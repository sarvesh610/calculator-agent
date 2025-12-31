"""Calculator agent that uses tools to perform calculations"""
from typing import Any
from anthropic import Anthropic
from ..config.settings import settings
from ..state.memory import Memory
from ..tools.calculator import AddNumbersTool, MultiplyNumbersTool, SubtractNumbersTool
from ..tools.memory_tools import SaveResultTool, RecallResultTool
from ..tools.base import BaseTool


class CalculatorAgent:
    """Agent that orchestrates calculator tools"""
    
    def __init__(self):
        self.client = Anthropic(api_key=settings.anthropic_api_key)
        self.memory = Memory()
        
        # Initialize tools
        self.tools: list[BaseTool] = [
            AddNumbersTool(self.memory),
            MultiplyNumbersTool(self.memory),
            SaveResultTool(self.memory),
            RecallResultTool(self.memory),
            SubtractNumbersTool(self.memory)
        ]
        
        # Build tool definitions for Claude
        self.tool_definitions = self._build_tool_definitions()
        
        # System prompt
        self.system_prompt = """You are a helpful calculator assistant. You have access to tools for math operations.

When the user refers to "that" or "it" or "the result", they mean the most recent calculation result.

Guidelines:
- Use add_numbers for addition
- Use multiply_numbers for multiplication  
- Use save_result to save values with names
- Use recall_result to retrieve saved values
- When user says "multiply that" or "add to that", use the last calculation result

Be concise and friendly in your responses."""
    
    def _build_tool_definitions(self) -> list[dict[str, Any]]:
        """Convert our tools to Anthropic's tool format"""
        definitions = []
        
        for tool in self.tools:
            if tool.name in ["add_numbers", "multiply_numbers", "subtract_numbers"]:
                schema = {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number",
                            "description": "First number"
                        },
                        "b": {
                            "type": "number",
                            "description": "Second number"
                        }
                    },
                    "required": ["a", "b"]
                }
            elif tool.name == "save_result":
                schema = {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name to save the result under"
                        },
                        "value": {
                            "type": "number",
                            "description": "Value to save"
                        }
                    },
                    "required": ["name", "value"]
                }
            elif tool.name == "recall_result":
                schema = {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of the saved result to recall"
                        }
                    },
                    "required": ["name"]
                }
            
            definitions.append({
                "name": tool.name,
                "description": tool.description,
                "input_schema": schema
            })
        
        return definitions
    
    def _get_tool_by_name(self, name: str) -> BaseTool | None:
        """Get a tool by its name"""
        for tool in self.tools:
            if tool.name == name:
                return tool
        return None
    
    def _build_context_message(self) -> str:
        """Build context about current state"""
        context_parts = []
        
        # Add last result if exists
        last_result = self.memory.get_last_result()
        if last_result is not None:
            context_parts.append(f"Most recent calculation result: {last_result}")
        
        # Add saved results if any
        saved = self.memory.list_saved_results()
        if saved:
            saved_str = ", ".join([f"{name}={result.value}" for name, result in saved.items()])
            context_parts.append(f"Saved results: {saved_str}")
        
        if context_parts:
            return "Context: " + " | ".join(context_parts)
        return ""
    
    def run(self, user_message: str) -> str:
        """
        Run the agent with a user message
        
        Args:
            user_message: The user's input
            
        Returns:
            The agent's response
        """
        # Build user message with context
        context = self._build_context_message()
        full_message = f"{context}\n\nUser: {user_message}" if context else user_message
        
        messages = [{"role": "user", "content": full_message}]
        
        # Agent loop: may require multiple tool calls
        while True:
            response = self.client.messages.create(
                model=settings.model_name,
                max_tokens=settings.max_tokens,
                temperature=settings.temperature,
                system=self.system_prompt,
                tools=self.tool_definitions,
                messages=messages
            )
            
            # Check if Claude wants to use a tool
            if response.stop_reason == "tool_use":
                # Find the tool use block
                tool_use = None
                for block in response.content:
                    if block.type == "tool_use":
                        tool_use = block
                        break
                
                if tool_use:
                    # Get the tool
                    tool = self._get_tool_by_name(tool_use.name)
                    if not tool:
                        return f"Error: Unknown tool {tool_use.name}"
                    
                    # Execute the tool
                    from ..models.schemas import (
                        MathOperationInput,
                        SaveResultInput,
                        RecallResultInput
                    )
                    
                    # Map input based on tool type
                    if tool.name in ["add_numbers", "multiply_numbers", "subtract_numbers"]:
                        tool_input = MathOperationInput(**tool_use.input)
                    elif tool.name == "save_result":
                        tool_input = SaveResultInput(**tool_use.input)
                    elif tool.name == "recall_result":
                        tool_input = RecallResultInput(**tool_use.input)
                    
                    # Execute
                    result = tool.execute(tool_input)
                    
                    # Add tool result to messages
                    messages.append({"role": "assistant", "content": response.content})
                    messages.append({
                        "role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": result.message
                        }]
                    })
                    
                    # Continue the loop - Claude will process the result
                    continue
            
            # No more tool calls - extract final response
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            
            return "I couldn't generate a response."
    
    def get_conversation_history(self) -> list[str]:
        """Get the conversation history"""
        return self.memory.get_history()
    
    def get_saved_results(self) -> dict:
        """Get all saved results"""
        results = self.memory.list_saved_results()
        return {name: result.value for name, result in results.items()}
    
    def clear_memory(self) -> None:
        """Clear all memory"""
        self.memory.clear()

"""Calculator tools for basic math operations"""
from typing import TYPE_CHECKING
from .base import BaseTool
from ..models.schemas import MathOperationInput, ToolOutput

if TYPE_CHECKING:
    from ..state.memory import Memory


class AddNumbersTool(BaseTool):
    """Tool for adding two numbers"""
    
    def __init__(self, memory: "Memory"):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "add_numbers"
    
    @property
    def description(self) -> str:
        return (
            "Add two numbers together. "
            "Use this when the user asks to add, sum, or plus numbers. "
            "Returns the sum of a and b."
        )
    
    def execute(self, input_data: MathOperationInput) -> ToolOutput:
        """Add two numbers and store result"""
        try:
            result = input_data.a + input_data.b
            
            # Store as last result for "multiply that by X" scenarios
            self.memory.set_last_result(result)
            self.memory.add_to_history(
                f"Added {input_data.a} + {input_data.b} = {result}"
            )
            
            return ToolOutput(
                success=True,
                result=result,
                message=f"{input_data.a} + {input_data.b} = {result}"
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                error=str(e),
                message=f"Failed to add numbers: {e}"
            )


class MultiplyNumbersTool(BaseTool):
    """Tool for multiplying two numbers"""
    
    def __init__(self, memory: "Memory"):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "multiply_numbers"
    
    @property
    def description(self) -> str:
        return (
            "Multiply two numbers together. "
            "Use this when the user asks to multiply, times, or find the product. "
            "Returns the product of a and b."
        )
    
    def execute(self, input_data: MathOperationInput) -> ToolOutput:
        """Multiply two numbers and store result"""
        try:
            result = input_data.a * input_data.b
            
            # Store as last result
            self.memory.set_last_result(result)
            self.memory.add_to_history(
                f"Multiplied {input_data.a} × {input_data.b} = {result}"
            )
            
            return ToolOutput(
                success=True,
                result=result,
                message=f"{input_data.a} × {input_data.b} = {result}"
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                error=str(e),
                message=f"Failed to multiply numbers: {e}"
            )
        
class SubtractNumbersTool(BaseTool):
    """Tool for subtracting numbers"""
    
    def __init__(self, memory: "Memory"):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "subtract_numbers"
    
    @property
    def description(self) -> str:
        return (
            "Subtract b from a. Returns a - b. "
            "Use this when the user asks to subtract numbers."
        )
    
    def execute(self, input_data: MathOperationInput) -> ToolOutput:
        """Subtract b from a and store result"""
        try:
            result = input_data.a - input_data.b
            
            # Store as last result
            self.memory.set_last_result(result)
            
            # Add to history
            self.memory.add_to_history(
                f"Subtracted {input_data.b} from {input_data.a} = {result}"
            )
            
            return ToolOutput(
                success=True,
                result=result,
                message=f"{input_data.a} - {input_data.b} = {result}"
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                error=str(e),
                message=f"Failed to subtract numbers: {e}"
            )

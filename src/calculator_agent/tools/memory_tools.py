"""Tools for saving and recalling results"""
from typing import TYPE_CHECKING
from .base import BaseTool
from ..models.schemas import SaveResultInput, RecallResultInput, ToolOutput

if TYPE_CHECKING:
    from ..state.memory import Memory


class SaveResultTool(BaseTool):
    """Tool for saving a named result"""
    
    def __init__(self, memory: "Memory"):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "save_result"
    
    @property
    def description(self) -> str:
        return (
            "Save a calculation result with a name for later recall. "
            "Use this when the user asks to save, store, or remember a value. "
            "Example: 'save 42 as my_number' or 'remember this as total'"
        )
    
    def execute(self, input_data: SaveResultInput) -> ToolOutput:
        """Save a result with a name"""
        try:
            self.memory.save_result(input_data.name, input_data.value)
            self.memory.add_to_history(
                f"Saved {input_data.value} as '{input_data.name}'"
            )
            
            return ToolOutput(
                success=True,
                result=input_data.value,
                message=f"Saved {input_data.value} as '{input_data.name}'"
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                error=str(e),
                message=f"Failed to save result: {e}"
            )


class RecallResultTool(BaseTool):
    """Tool for recalling a saved result"""
    
    def __init__(self, memory: "Memory"):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "recall_result"
    
    @property
    def description(self) -> str:
        return (
            "Recall a previously saved result by name. "
            "Use this when the user asks 'what was X?' or 'recall Y'. "
            "Returns the saved value if it exists."
        )
    
    def execute(self, input_data: RecallResultInput) -> ToolOutput:
        """Recall a saved result by name"""
        try:
            result = self.memory.recall_result(input_data.name)
            
            if result is None:
                return ToolOutput(
                    success=False,
                    message=f"No saved result found with name '{input_data.name}'"
                )
            
            self.memory.add_to_history(
                f"Recalled '{input_data.name}' = {result.value}"
            )
            
            return ToolOutput(
                success=True,
                result=result.value,
                message=f"'{result.name}' = {result.value} (saved at {result.timestamp})"
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                error=str(e),
                message=f"Failed to recall result: {e}"
            )

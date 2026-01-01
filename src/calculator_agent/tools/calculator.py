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
class DivideNumbersTool(BaseTool):
    """Tool for dividing numbers with error handling"""
    
    def __init__(self, memory: "Memory"):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "divide_numbers"
    
    @property
    def description(self) -> str:
        return (
            "Divide a by b. Returns a / b. "
            "Use this when the user asks to divide numbers. "
            "Handles division by zero gracefully."
        )
    
    def execute(self, input_data: MathOperationInput) -> ToolOutput:
        """Divide with error handling"""
        try:
            # Validate: Check for division by zero
            if input_data.b == 0:
                return ToolOutput(
                    success=False,
                    error="division_by_zero",
                    message="Cannot divide by zero. Please provide a non-zero divisor."
                )
            
            result = input_data.a / input_data.b
            
            # Store result
            self.memory.set_last_result(result)
            self.memory.add_to_history(
                f"Divided {input_data.a} by {input_data.b} = {result}"
            )
            
            return ToolOutput(
                success=True,
                result=result,
                message=f"{input_data.a} ÷ {input_data.b} = {result}"
            )
            
        except Exception as e:
            # Catch any other errors
            return ToolOutput(
                success=False,
                error=str(e),
                message=f"Error dividing numbers: {e}"
            )
class PowerNumbersTool(BaseTool):
    """Tool for raising a number to a power"""
    
    def __init__(self, memory: "Memory"):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "power_numbers"
    
    @property
    def description(self) -> str:
        return (
            "Raise a to the power of b. Returns a^b. "
            "Use this when the user asks for exponents, powers, squared, cubed, etc. "
            "Example: 'What's 2 to the power of 8?' or '5 squared'"
        )
    
    def execute(self, input_data: MathOperationInput) -> ToolOutput:
        """Calculate power with error handling"""
        try:
            result = input_data.a ** input_data.b
            
            # Check for overflow or invalid results
            if result == float('inf') or result == float('-inf'):
                return ToolOutput(
                    success=False,
                    error="overflow",
                    message=f"Result too large: {input_data.a}^{input_data.b} causes overflow"
                )
            
            # Store result
            self.memory.set_last_result(result)
            self.memory.add_to_history(
                f"Calculated {input_data.a} ^ {input_data.b} = {result}"
            )
            
            return ToolOutput(
                success=True,
                result=result,
                message=f"{input_data.a}^{input_data.b} = {result}"
            )
            
        except Exception as e:
            return ToolOutput(
                success=False,
                error=str(e),
                message=f"Error calculating power: {e}"
            )

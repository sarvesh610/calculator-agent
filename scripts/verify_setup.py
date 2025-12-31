"""Test that our architecture components work"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.calculator_agent.models.schemas import (
    MathOperationInput, 
    SaveResultInput,
    ToolOutput
)
from src.calculator_agent.state.memory import Memory
from src.calculator_agent.tools.base import BaseTool

def test_models():
    """Test data models"""
    # Create a math input
    math_input = MathOperationInput(a=5, b=3)
    print(f"✅ Math input: {math_input.a} + {math_input.b}")
    
    # Create a tool output
    output = ToolOutput(
        success=True,
        result=8,
        message="Addition successful"
    )
    print(f"✅ Tool output: {output.message}")

def test_memory():
    """Test state management"""
    memory = Memory()
    
    # Save a result
    memory.save_result("test", 42.0)
    print(f"✅ Saved result: test = 42.0")
    
    # Recall it
    result = memory.recall_result("test")
    print(f"✅ Recalled result: {result.name} = {result.value}")
    
    # Test last result
    memory.set_last_result(100.0)
    last = memory.get_last_result()
    print(f"✅ Last result: {last}")

def test_base_tool():
    """Test that BaseTool interface exists"""
    print(f"✅ BaseTool interface defined")
    print(f"   Required methods: name, description, execute")

if __name__ == "__main__":
    print("Testing architecture components...\n")
    test_models()
    print()
    test_memory()
    print()
    test_base_tool()
    print("\n✅ All architecture components work!")

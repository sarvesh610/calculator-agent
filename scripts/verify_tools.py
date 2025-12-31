"""Test individual tools"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.calculator_agent.state.memory import Memory
from src.calculator_agent.tools.calculator import AddNumbersTool, MultiplyNumbersTool
from src.calculator_agent.tools.memory_tools import SaveResultTool, RecallResultTool
from src.calculator_agent.models.schemas import (
    MathOperationInput,
    SaveResultInput,
    RecallResultInput
)


def test_add_tool():
    """Test addition tool"""
    print("Testing AddNumbersTool...")
    memory = Memory()
    tool = AddNumbersTool(memory)
    
    # Test addition
    result = tool.execute(MathOperationInput(a=15, b=27))
    assert result.success, "Addition should succeed"
    assert result.result == 42, f"Expected 42, got {result.result}"
    print(f"  ✅ {result.message}")
    
    # Verify last result was stored
    assert memory.get_last_result() == 42, "Last result should be 42"
    print(f"  ✅ Last result stored: {memory.get_last_result()}")


def test_multiply_tool():
    """Test multiplication tool"""
    print("\nTesting MultiplyNumbersTool...")
    memory = Memory()
    tool = MultiplyNumbersTool(memory)
    
    # Test multiplication
    result = tool.execute(MathOperationInput(a=6, b=7))
    assert result.success, "Multiplication should succeed"
    assert result.result == 42, f"Expected 42, got {result.result}"
    print(f"  ✅ {result.message}")


def test_save_and_recall():
    """Test save and recall tools"""
    print("\nTesting SaveResultTool and RecallResultTool...")
    memory = Memory()
    save_tool = SaveResultTool(memory)
    recall_tool = RecallResultTool(memory)
    
    # Save a result
    save_result = save_tool.execute(SaveResultInput(name="my_number", value=42.0))
    assert save_result.success, "Save should succeed"
    print(f"  ✅ {save_result.message}")
    
    # Recall the result
    recall_result = recall_tool.execute(RecallResultInput(name="my_number"))
    assert recall_result.success, "Recall should succeed"
    assert recall_result.result == 42.0, f"Expected 42.0, got {recall_result.result}"
    print(f"  ✅ {recall_result.message}")
    
    # Try to recall non-existent result
    no_result = recall_tool.execute(RecallResultInput(name="nonexistent"))
    assert not no_result.success, "Should fail for non-existent result"
    print(f"  ✅ Correctly failed for non-existent result")


def test_conversation_flow():
    """Test a realistic conversation flow"""
    print("\nTesting conversation flow...")
    memory = Memory()
    add_tool = AddNumbersTool(memory)
    multiply_tool = MultiplyNumbersTool(memory)
    save_tool = SaveResultTool(memory)
    
    # User: "What's 15 plus 27?"
    result1 = add_tool.execute(MathOperationInput(a=15, b=27))
    print(f"  Step 1: {result1.message}")
    
    # User: "Multiply that by 3"
    last_result = memory.get_last_result()
    result2 = multiply_tool.execute(MathOperationInput(a=last_result, b=3))
    print(f"  Step 2: {result2.message}")
    
    # User: "Save that as total"
    final_result = memory.get_last_result()
    result3 = save_tool.execute(SaveResultInput(name="total", value=final_result))
    print(f"  Step 3: {result3.message}")
    
    # Verify
    assert result2.result == 126, "Should be 126"
    print(f"  ✅ Conversation flow works correctly!")
    
    # Show history
    print("\n  Conversation history:")
    for entry in memory.get_history():
        print(f"    - {entry}")


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING CALCULATOR AGENT TOOLS")
    print("=" * 60)
    
    test_add_tool()
    test_multiply_tool()
    test_save_and_recall()
    test_conversation_flow()
    
    print("\n" + "=" * 60)
    print("✅ ALL TOOL TESTS PASSED!")
    print("=" * 60)

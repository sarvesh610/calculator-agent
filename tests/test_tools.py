"""Pytest unit tests for calculator tools"""
import pytest
from src.calculator_agent.state.memory import Memory
from src.calculator_agent.tools.calculator import AddNumbersTool, MultiplyNumbersTool, SubtractNumbersTool, DivideNumbersTool, PowerNumbersTool
from src.calculator_agent.tools.memory_tools import SaveResultTool, RecallResultTool
from src.calculator_agent.models.schemas import (
    MathOperationInput,
    SaveResultInput,
    RecallResultInput
)


class TestAddNumbersTool:
    """Tests for AddNumbersTool"""
    
    def test_add_positive_numbers(self):
        memory = Memory()
        tool = AddNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=5, b=3))
        
        assert result.success is True
        assert result.result == 8
        assert memory.get_last_result() == 8
    
    def test_add_negative_numbers(self):
        memory = Memory()
        tool = AddNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=-5, b=-3))
        
        assert result.success is True
        assert result.result == -8
    
    def test_add_stores_in_memory(self):
        memory = Memory()
        tool = AddNumbersTool(memory)
        tool.execute(MathOperationInput(a=10, b=20))
        
        assert memory.get_last_result() == 30
        assert len(memory.get_history()) == 1


class TestMultiplyNumbersTool:
    """Tests for MultiplyNumbersTool"""
    
    def test_multiply_positive_numbers(self):
        memory = Memory()
        tool = MultiplyNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=6, b=7))
        
        assert result.success is True
        assert result.result == 42
    
    def test_multiply_by_zero(self):
        memory = Memory()
        tool = MultiplyNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=5, b=0))
        
        assert result.success is True
        assert result.result == 0


class TestSaveResultTool:
    """Tests for SaveResultTool"""
    
    def test_save_result(self):
        memory = Memory()
        tool = SaveResultTool(memory)
        result = tool.execute(SaveResultInput(name="test", value=42.0))
        
        assert result.success is True
        assert memory.recall_result("test").value == 42.0
    
    def test_overwrite_saved_result(self):
        memory = Memory()
        tool = SaveResultTool(memory)
        
        tool.execute(SaveResultInput(name="test", value=10.0))
        tool.execute(SaveResultInput(name="test", value=20.0))
        
        assert memory.recall_result("test").value == 20.0


class TestRecallResultTool:
    """Tests for RecallResultTool"""
    
    def test_recall_existing_result(self):
        memory = Memory()
        save_tool = SaveResultTool(memory)
        recall_tool = RecallResultTool(memory)
        
        save_tool.execute(SaveResultInput(name="answer", value=42.0))
        result = recall_tool.execute(RecallResultInput(name="answer"))
        
        assert result.success is True
        assert result.result == 42.0
    
    def test_recall_nonexistent_result(self):
        memory = Memory()
        tool = RecallResultTool(memory)
        result = tool.execute(RecallResultInput(name="nonexistent"))
        
        assert result.success is False
        assert result.result is None


class TestConversationFlow:
    """Integration tests for tool flows"""
    
    def test_add_then_multiply_flow(self):
        """Test: add two numbers, then multiply result"""
        memory = Memory()
        add_tool = AddNumbersTool(memory)
        multiply_tool = MultiplyNumbersTool(memory)
        
        # Add 15 + 27 = 42
        add_tool.execute(MathOperationInput(a=15, b=27))
        
        # Multiply 42 * 3 = 126
        last_result = memory.get_last_result()
        result = multiply_tool.execute(MathOperationInput(a=last_result, b=3))
        
        assert result.result == 126
    
    def test_calculate_save_recall_flow(self):
        """Test: calculate, save, then recall"""
        memory = Memory()
        add_tool = AddNumbersTool(memory)
        save_tool = SaveResultTool(memory)
        recall_tool = RecallResultTool(memory)
        
        # Calculate
        add_tool.execute(MathOperationInput(a=10, b=20))
        
        # Save
        last = memory.get_last_result()
        save_tool.execute(SaveResultInput(name="my_total", value=last))
        
        # Recall
        result = recall_tool.execute(RecallResultInput(name="my_total"))
        
        assert result.result == 30
class TestDivideNumbersTool:
    """Tests for DivideNumbersTool"""
    
    def test_divide_positive_numbers(self):
        memory = Memory()
        tool = DivideNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=10, b=2))
        
        assert result.success is True
        assert result.result == 5
        assert memory.get_last_result() == 5
    
    def test_divide_by_zero(self):
        memory = Memory()
        tool = DivideNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=10, b=0))
        
        assert result.success is False
        assert result.error == "division_by_zero"
        assert "Cannot divide by zero" in result.message
    
    def test_divide_negative_numbers(self):
        memory = Memory()
        tool = DivideNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=-10, b=2))
        
        assert result.success is True
        assert result.result == -5


class TestPowerNumbersTool:
    """Tests for PowerNumbersTool"""
    
    def test_power_positive_integers(self):
        memory = Memory()
        tool = PowerNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=2, b=8))
        
        assert result.success is True
        assert result.result == 256
    
    def test_power_squared(self):
        memory = Memory()
        tool = PowerNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=5, b=2))
        
        assert result.success is True
        assert result.result == 25
    
    def test_power_cubed(self):
        memory = Memory()
        tool = PowerNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=3, b=3))
        
        assert result.success is True
        assert result.result == 27
    
    def test_power_zero(self):
        memory = Memory()
        tool = PowerNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=10, b=0))
        
        assert result.success is True
        assert result.result == 1  # Anything to the power of 0 is 1
    
    def test_power_negative_exponent(self):
        memory = Memory()
        tool = PowerNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=2, b=-2))
        
        assert result.success is True
        assert result.result == 0.25  # 2^-2 = 1/4
# Add this test class after TestMultiplyNumbersTool
class TestSubtractNumbersTool:
    """Tests for SubtractNumbersTool"""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers"""
        memory = Memory()
        tool = SubtractNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=10, b=3))
        
        assert result.success is True
        assert result.result == 7
        assert memory.get_last_result() == 7
    
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number"""
        memory = Memory()
        tool = SubtractNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=5, b=10))
        
        assert result.success is True
        assert result.result == -5
        assert memory.get_last_result() == -5
    
    def test_subtract_from_zero(self):
        """Test subtracting from zero"""
        memory = Memory()
        tool = SubtractNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=0, b=5))
        
        assert result.success is True
        assert result.result == -5
    
    def test_subtract_zero(self):
        """Test subtracting zero"""
        memory = Memory()
        tool = SubtractNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=10, b=0))
        
        assert result.success is True
        assert result.result == 10
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        memory = Memory()
        tool = SubtractNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=-5, b=-3))
        
        assert result.success is True
        assert result.result == -2  # -5 - (-3) = -5 + 3 = -2
    
    def test_subtract_stores_in_memory(self):
        """Test that result is stored in memory"""
        memory = Memory()
        tool = SubtractNumbersTool(memory)
        tool.execute(MathOperationInput(a=100, b=25))
        
        assert memory.get_last_result() == 75
        assert len(memory.get_history()) == 1
        assert "Subtracted 25.0 from 100.0 = 75.0" in memory.get_history()[0]
    
    def test_subtract_decimal_numbers(self):
        """Test subtracting decimal numbers"""
        memory = Memory()
        tool = SubtractNumbersTool(memory)
        result = tool.execute(MathOperationInput(a=10.5, b=3.2))
        
        assert result.success is True
        assert result.result == pytest.approx(7.3, rel=1e-9)

"""Base tool interface for the calculator agent"""
from abc import ABC, abstractmethod
from typing import Any
from ..models.schemas import ToolInput, ToolOutput


class BaseTool(ABC):
    """Base class for all tools"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Tool name for the agent to reference"""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Description of what the tool does"""
        pass
    
    @abstractmethod
    def execute(self, input_data: ToolInput) -> ToolOutput:
        """
        Execute the tool with given input
        
        Args:
            input_data: Validated input for the tool
            
        Returns:
            ToolOutput with success status, result, and message
        """
        pass
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

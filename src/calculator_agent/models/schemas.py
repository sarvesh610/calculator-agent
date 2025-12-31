"""Data models for the calculator agent"""
from typing import Any, Optional
from pydantic import BaseModel, Field


class ToolInput(BaseModel):
    """Base class for tool inputs"""
    pass


class ToolOutput(BaseModel):
    """Standard tool output format"""
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None
    message: str


class MathOperationInput(ToolInput):
    """Input for math operations"""
    a: float = Field(description="First number")
    b: float = Field(description="Second number")


class SaveResultInput(ToolInput):
    """Input for saving a result"""
    name: str = Field(description="Name to save the result under")
    value: float = Field(description="Value to save")


class RecallResultInput(ToolInput):
    """Input for recalling a saved result"""
    name: str = Field(description="Name of the saved result to recall")


class SavedResult(BaseModel):
    """A saved calculation result"""
    name: str
    value: float
    timestamp: str

"""State management for the calculator agent"""
from typing import Dict, Optional
from datetime import datetime
from ..models.schemas import SavedResult


class Memory:
    """Manages conversation state and saved results"""
    
    def __init__(self):
        self._saved_results: Dict[str, SavedResult] = {}
        self._last_result: Optional[float] = None
        self._conversation_history: list[str] = []
    
    def save_result(self, name: str, value: float) -> None:
        """Save a named result"""
        self._saved_results[name] = SavedResult(
            name=name,
            value=value,
            timestamp=datetime.now().isoformat()
        )
        self._last_result = value
    
    def recall_result(self, name: str) -> Optional[SavedResult]:
        """Recall a saved result by name"""
        return self._saved_results.get(name)
    
    def get_last_result(self) -> Optional[float]:
        """Get the most recent calculation result"""
        return self._last_result
    
    def set_last_result(self, value: float) -> None:
        """Set the most recent result"""
        self._last_result = value
    
    def list_saved_results(self) -> Dict[str, SavedResult]:
        """Get all saved results"""
        return self._saved_results.copy()
    
    def add_to_history(self, entry: str) -> None:
        """Add an entry to conversation history"""
        self._conversation_history.append(entry)
    
    def get_history(self) -> list[str]:
        """Get conversation history"""
        return self._conversation_history.copy()
    
    def clear(self) -> None:
        """Clear all state"""
        self._saved_results.clear()
        self._last_result = None
        self._conversation_history.clear()

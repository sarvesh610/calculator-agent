"""Logging utilities for the calculator agent"""
import logging
import sys
from datetime import datetime
from typing import Any


class AgentLogger:
    """Custom logger for agent operations"""
    
    def __init__(self, name: str = "calculator_agent", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Remove existing handlers
        self.logger.handlers.clear()
        
        # Console handler with custom formatting
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        
        # Custom format with colors
        formatter = ColoredFormatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
        self.logger.propagate = False
    
    def agent_thinking(self, message: str) -> None:
        """Log when agent is processing"""
        self.logger.info(f"🤔 THINKING: {message}")
    
    def tool_call(self, tool_name: str, inputs: dict) -> None:
        """Log when a tool is being called"""
        self.logger.info(f"🔧 TOOL CALL: {tool_name}({inputs})")
    
    def tool_result(self, tool_name: str, success: bool, result: Any) -> None:
        """Log tool execution result"""
        status = "✅ SUCCESS" if success else "❌ FAILED"
        self.logger.info(f"{status}: {tool_name} → {result}")
    
    def agent_response(self, response: str) -> None:
        """Log final agent response"""
        self.logger.info(f"💬 RESPONSE: {response[:100]}{'...' if len(response) > 100 else ''}")
    
    def error(self, message: str, exception: Exception = None) -> None:
        """Log errors"""
        self.logger.error(f"🚨 ERROR: {message}")
        if exception:
            self.logger.error(f"   Exception: {exception}")
    
    def debug(self, message: str) -> None:
        """Log debug information"""
        self.logger.debug(f"🔍 DEBUG: {message}")


class ColoredFormatter(logging.Formatter):
    """Custom formatter with colors for terminal output"""
    
    # ANSI color codes
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
    }
    RESET = '\033[0m'
    
    def format(self, record):
        # Add color to level name
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{levelname}{self.RESET}"
        
        return super().format(record)


# Global logger instance
agent_logger = AgentLogger()

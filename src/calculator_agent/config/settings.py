"""Configuration settings for the calculator agent"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment"""
    
    anthropic_api_key: str
    model_name: str = "claude-sonnet-4-20250514"
    max_tokens: int = 1024
    temperature: float = 0.0  # Deterministic for math
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


# Global settings instance
settings = Settings()

# Storage Options for Calculator Agent

## Current: In-Memory
- **Location:** `src/calculator_agent/state/memory.py`
- **Pros:** Fast, simple, no setup
- **Cons:** Lost on restart
- **Use for:** Local development, testing

## Future Options

### SQLite (Local Persistence)
- **When:** Need data to survive restarts
- **Implementation:** `src/calculator_agent/state/db_storage.py`
- **Use for:** Local testing, single-user apps

### Redis (Production)
- **When:** Deploying to production, multiple servers
- **Implementation:** `src/calculator_agent/state/redis_storage.py`
- **Use for:** Production deployments

### PostgreSQL (Enterprise)
- **When:** Complex queries, multi-user, enterprise scale
- **Use for:** Large-scale production systems

## Interface Contract

All storage implementations must provide:
```python
def save_result(name: str, value: float) -> None
def recall_result(name: str) -> Optional[SavedResult]
def get_last_result() -> Optional[float]
def set_last_result(value: float) -> None
def add_to_history(entry: str) -> None
def get_history() -> list[str]
def clear() -> None
```

This allows swapping storage without changing agent code.

# Calculator Agent

An AI-powered calculator agent built with Claude that demonstrates tool-based architecture, state management, and agentic decision-making.

## 🎯 What This Is

A conversational calculator that:
- Performs math operations through natural language
- Remembers previous calculations
- Saves and recalls named results
- Demonstrates core AI agent patterns
- Handles errors gracefully

**Example conversation:**
```
You: What's 15 plus 27?
Agent: 15 plus 27 equals 42.

You: Multiply that by 3
Agent: The result is 126.0

You: Divide that by 2
Agent: The result is 63.0

You: What's 5 squared?
Agent: 5 squared equals 25.

You: Save that as my_number
Agent: I've saved 25.0 as "my_number" for you!

You: What was my_number?
Agent: Your saved value "my_number" is 25.0

You: Divide 10 by 0
Agent: I can't divide 10 by 0 because division by zero is undefined.
```

---

## 🏗️ Architecture
```
calculator-agent/
├── src/calculator_agent/
│   ├── config/          # Configuration & settings
│   │   └── settings.py
│   ├── models/          # Data structures (Pydantic models)
│   │   └── schemas.py
│   ├── state/           # Memory/state management
│   │   └── memory.py
│   ├── tools/           # Individual tool implementations
│   │   ├── base.py          # Base tool interface
│   │   ├── calculator.py    # Math tools (5 operations)
│   │   └── memory_tools.py  # Save/recall tools
│   └── agents/          # Agent orchestrator
│       └── calculator_agent.py
├── tests/               # Pytest unit tests (24 tests)
├── scripts/             # Verification scripts
├── docs/                # Documentation
├── main.py              # Entry point
├── pyproject.toml       # Dependencies
└── .env                 # API keys (git ignored)
```

---

## 📋 Prerequisites

### Required
- **Python 3.11+** 
- **Anthropic API Key** (get from [console.anthropic.com](https://console.anthropic.com))
- **uv** (modern Python package manager)

### System Requirements
- macOS, Linux, or Windows
- ~50MB disk space
- Internet connection (for API calls)

---

## 🚀 Quick Start

### 1. Install Python 3.11+

**macOS:**
```bash
brew install python@3.11
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11
```

**Windows:**
Download from [python.org](https://www.python.org/downloads/)

**Verify:**
```bash
python3 --version  # Should show 3.11 or higher
```

---

### 2. Install uv (Package Manager)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Verify:**
```bash
uv --version
```

---

### 3. Set Up Project
```bash
# Navigate to project directory
cd calculator-agent

# Install all dependencies
uv sync --all-extras
```

This installs:
- `anthropic` - Claude API client
- `langchain` & `langchain-anthropic` - Agent framework
- `pydantic` - Data validation
- `python-dotenv` - Environment variables
- `pytest`, `black`, `ruff`, `mypy` - Development tools

---

### 4. Configure API Key

**Get your API key:**
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up / Log in
3. Navigate to "API Keys"
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-api03-...`)

**⚠️ Note:** You need to add **$5 minimum credit** to activate API access

**Create `.env` file:**
```bash
# Copy the example template
cp .env.example .env

# Edit the file
nano .env
# or
code .env
```

**Add your key:**
```
ANTHROPIC_API_KEY=sk-ant-api03-your-actual-key-here
```

**⚠️ IMPORTANT:** Never commit `.env` to git! It's already in `.gitignore`.

---

### 5. Test Setup
```bash
# Quick API test
uv run python scripts/verify_api.py
```

**Expected output:**
```
✅ API key loaded (starts with: sk-ant-api03-...)
✅ API connection successful!
✅ Claude says: Setup complete!
```

If you see this, you're ready to go! 🎉

---

## ▶️ Running the Agent

### Start Interactive Mode
```bash
uv run python main.py
```

**You'll see:**
```
============================================================
CALCULATOR AGENT
============================================================
I can help you with calculations!
Try: 'What's 15 plus 27?'
     'Multiply that by 3'
     'Save that as my_total'
     'What was my_total?'

Type 'quit' to exit, 'history' to see conversation
============================================================

You: 
```

### Commands

| Command | Description |
|---------|-------------|
| `quit` or `exit` | Exit the program |
| `history` | View conversation history |
| `saved` | View all saved results |

### Example Session
```
You: What's 100 minus 25?
Agent: 100 minus 25 equals 75.

You: Divide that by 5
Agent: The result is 15.0

You: What's 2 to the power of 8?
Agent: 2 to the power of 8 equals 256.

You: Multiply that by 3
Agent: The result is 768.0

You: Save that as result
Agent: I've saved 768.0 as "result" for you!

You: Divide 10 by 0
Agent: I can't divide 10 by 0 because division by zero is undefined.

You: history
Conversation History:
  - Subtracted 25.0 from 100.0 = 75.0
  - Divided 75.0 by 5.0 = 15.0
  - Calculated 2.0 ^ 8.0 = 256.0
  - Multiplied 256.0 × 3.0 = 768.0
  - Saved 768.0 as 'result'

You: saved
Saved Results:
  result = 768.0

You: quit
Goodbye!
```

---

## 🧪 Testing

### Run Full Test Suite
```bash
# Run all pytest tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run with coverage
uv run pytest --cov=src --cov-report=term-missing
```

### Run Verification Scripts
```bash
# Verify API connection
uv run python scripts/verify_api.py

# Verify project setup
uv run python scripts/verify_setup.py

# Verify tools manually
uv run python scripts/verify_tools.py
```

### Expected Test Output
```
======================== test session starts ========================
tests/test_memory.py::TestMemory::test_initial_state PASSED
tests/test_memory.py::TestMemory::test_save_and_recall_result PASSED
tests/test_tools.py::TestAddNumbersTool::test_add_positive_numbers PASSED
tests/test_tools.py::TestMultiplyNumbersTool::test_multiply_positive_numbers PASSED
tests/test_tools.py::TestSubtractNumbersTool::test_subtract_positive_numbers PASSED
tests/test_tools.py::TestDivideNumbersTool::test_divide_positive_numbers PASSED
tests/test_tools.py::TestDivideNumbersTool::test_divide_by_zero PASSED
tests/test_tools.py::TestPowerNumbersTool::test_power_positive_integers PASSED
tests/test_tools.py::TestPowerNumbersTool::test_power_squared PASSED
... (24 tests total)
======================== 24 passed in 0.5s =========================
```

---

## 🛠️ Available Tools

The agent currently has **7 tools** available:

### Math Operations (5 tools)

#### 1. Add Numbers
**Usage:** "What's 5 plus 3?", "Add 10 and 20"
```python
AddNumbersTool(a, b) → a + b
```

#### 2. Multiply Numbers
**Usage:** "Multiply 6 by 7", "What's 4 times 5?"
```python
MultiplyNumbersTool(a, b) → a × b
```

#### 3. Subtract Numbers
**Usage:** "What's 50 minus 8?", "Subtract 10 from that"
```python
SubtractNumbersTool(a, b) → a - b
```

#### 4. Divide Numbers
**Usage:** "Divide 100 by 4", "What's 72 divided by 6?"
- ✅ **Error handling:** Gracefully handles division by zero
```python
DivideNumbersTool(a, b) → a ÷ b
```

#### 5. Power/Exponent
**Usage:** "What's 2 to the power of 8?", "5 squared", "3 cubed"
- ✅ **Error handling:** Detects overflow for very large results
```python
PowerNumbersTool(a, b) → a^b
```

### Memory Operations (2 tools)

#### 6. Save Result
**Usage:** "Save that as total", "Remember this as my_number"
```python
SaveResultTool(name, value) → Saves value with name
```

#### 7. Recall Result
**Usage:** "What was total?", "Recall my_number"
```python
RecallResultTool(name) → Returns saved value
```

---

## 💰 Cost & API Usage

### Pricing

**Claude 3.5 Sonnet (model used):**
- Input: $3.00 per million tokens
- Output: $15.00 per million tokens

**Typical interaction:**
- ~350 tokens per turn
- Cost: ~$0.0015 per interaction
- **With $5 credit: ~3,300+ interactions**

### Rate Limits

- **Tier 1:** 50 requests/minute
- **Tier 2:** 1,000 requests/minute (after $5 spent)

For development, Tier 1 is more than sufficient.

---

## 🐛 Troubleshooting

### "No API key found!"

**Problem:** `.env` file missing or not configured

**Solution:**
```bash
# Check if .env exists
ls -la .env

# If not, create it
cp .env.example .env

# Edit and add your API key
nano .env
```

Make sure the file contains:
```
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

---

### "API test failed: authentication error"

**Problem:** Invalid or missing API key

**Solutions:**
1. **Check your key is correct:**
```bash
   cat .env
   # Should show: ANTHROPIC_API_KEY=sk-ant-api03-...
```

2. **Verify key on Anthropic console:**
   - Go to [console.anthropic.com](https://console.anthropic.com)
   - Check "API Keys" section
   - Ensure key is active and not deleted

3. **Regenerate key if needed:**
   - Delete old key on console
   - Create new key
   - Update `.env` file

---

### "ModuleNotFoundError: No module named 'anthropic'"

**Problem:** Dependencies not installed

**Solution:**
```bash
# Install dependencies
uv sync --all-extras

# Verify installation
uv run python -c "import anthropic; print('✅ anthropic installed')"
```

---

### Agent doesn't remember previous results

**Problem:** Memory is in-memory only (resets on restart)

**This is expected behavior!** 

Current implementation uses in-memory storage. To persist data:
1. See `docs/STORAGE_OPTIONS.md` for alternatives
2. Future sessions: We'll add SQLite/Redis for persistence

---

## 📚 Learning Resources

### Understanding the Code

- **`main.py`** - Entry point, interactive loop
- **`src/calculator_agent/agents/calculator_agent.py`** - Main agent logic, Claude SDK integration
- **`src/calculator_agent/tools/calculator.py`** - Math operation tools
- **`src/calculator_agent/tools/memory_tools.py`** - Save/recall tools
- **`src/calculator_agent/state/memory.py`** - State management

### Key Concepts

1. **Tool-based Architecture** - Each capability is a discrete tool
2. **Agent Loop** - Agent → Tool → Result → Response cycle
3. **State Management** - Memory shared across tools
4. **Error Handling** - Graceful failures (division by zero, overflow)
5. **Type Safety** - Pydantic validates all data

### Documentation

- [Anthropic API Docs](https://docs.anthropic.com/)
- [Anthropic Agent SDK](https://platform.claude.com/docs/en/agent-sdk/quickstart)
- [LangChain Docs](https://python.langchain.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)

---

## 🔮 Future Enhancements

### Session 3: Agent SDK Migration
- [ ] Refactor to Anthropic Agent SDK
- [ ] Implement pre/post handlers
- [ ] Add streaming responses
- [ ] Better error handling with middleware

### Session 4: Advanced Features
- [ ] Square root tool
- [ ] Modulo/remainder tool
- [ ] Persistent storage (SQLite/Redis)
- [ ] Conversation history with full context
- [ ] Web API (FastAPI)

### Session 5: Multi-Agent Systems
- [ ] Multiple specialized agents
- [ ] Agent-to-agent communication
- [ ] Product search agent (web search integration)
- [ ] Path to agentic commerce

---

## 📝 Development

### Adding New Tools

1. **Create tool class** in `src/calculator_agent/tools/calculator.py`:
```python
from .base import BaseTool
from ..models.schemas import MathOperationInput, ToolOutput

class ModuloNumbersTool(BaseTool):
    """Tool for modulo operation"""
    
    def __init__(self, memory):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "modulo_numbers"
    
    @property
    def description(self) -> str:
        return "Calculate a modulo b (remainder of a divided by b)."
    
    def execute(self, input_data: MathOperationInput) -> ToolOutput:
        try:
            if input_data.b == 0:
                return ToolOutput(
                    success=False,
                    error="division_by_zero",
                    message="Cannot calculate modulo with zero divisor"
                )
            
            result = input_data.a % input_data.b
            self.memory.set_last_result(result)
            self.memory.add_to_history(
                f"Calculated {input_data.a} mod {input_data.b} = {result}"
            )
            
            return ToolOutput(
                success=True,
                result=result,
                message=f"{input_data.a} mod {input_data.b} = {result}"
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                error=str(e),
                message=f"Error calculating modulo: {e}"
            )
```

2. **Register in agent** (`calculator_agent.py`):
```python
# Import
from ..tools.calculator import (..., ModuloNumbersTool)

# Add to tools list
self.tools = [
    ...,
    ModuloNumbersTool(self.memory),
]

# Update tool definitions
if tool.name in ["add_numbers", "multiply_numbers", "subtract_numbers", 
                 "divide_numbers", "power_numbers", "modulo_numbers"]:
    # ...

# Update input mapping
if tool.name in ["add_numbers", "multiply_numbers", "subtract_numbers", 
                 "divide_numbers", "power_numbers", "modulo_numbers"]:
    # ...
```

3. **Add tests** in `tests/test_tools.py`

---

## 📄 License

This is a learning project. Feel free to use and modify.

---

## ✅ Checklist: First Time Setup

- [ ] Python 3.11+ installed
- [ ] uv installed
- [ ] Project dependencies installed (`uv sync --all-extras`)
- [ ] `.env` file created with API key
- [ ] API test passes (`uv run python scripts/verify_api.py`)
- [ ] Agent runs successfully (`uv run python main.py`)
- [ ] All tests pass (`uv run pytest`)

**If all checkboxes are ✅, you're ready to go!** 🚀

---

## 📊 Project Stats

**Current Status:**
- ✅ **7 tools** implemented
  - 5 math operations (add, multiply, subtract, divide, power)
  - 2 memory operations (save, recall)
- ✅ **24 comprehensive unit tests**
  - 100% coverage of tool functionality
  - Edge case testing (division by zero, negative numbers, etc.)
- ✅ **Error handling**
  - Division by zero detection
  - Overflow detection
  - Graceful error messages
- ✅ **Full agent orchestration** with Claude SDK
- ✅ **In-memory state management**
- ✅ **Type-safe** with Pydantic
- ✅ **Professional structure**

**Learning Objectives Completed:**
- ✅ Tool-based architecture
- ✅ Agent decision-making and loops
- ✅ State management across conversations
- ✅ Error handling patterns
- ✅ Testing strategies
- ✅ Git workflow and version control

**Next Session:**
- Logging system (see agent reasoning)
- Agent SDK migration
- Streaming responses
- Product search agent (commerce path)


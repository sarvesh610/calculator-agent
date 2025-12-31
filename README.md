# Calculator Agent

An AI-powered calculator agent built with Claude that demonstrates tool-based architecture, state management, and agentic decision-making.

## 🎯 What This Is

A conversational calculator that:
- Performs math operations through natural language
- Remembers previous calculations
- Saves and recalls named results
- Demonstrates core AI agent patterns

**Example conversation:**
```
You: What's 15 plus 27?
Agent: 15 plus 27 equals 42.

You: Multiply that by 3
Agent: The result is 126.0

You: Save that as my_total
Agent: I've saved 126.0 as "my_total" for you!

You: What was my_total?
Agent: Your saved value "my_total" is 126.0.

You: Subtract 10 from that
Agent: The result is 116.0
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
│   │   ├── base.py      # Base tool interface
│   │   ├── calculator.py    # Math tools
│   │   └── memory_tools.py  # Save/recall tools
│   └── agents/          # Agent orchestrator
│       └── calculator_agent.py
├── tests/               # Pytest unit tests
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
# or
vim .env
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
You: What's 25 plus 17?
Agent: 25 plus 17 equals 42.

You: Multiply that by 2
Agent: The result is 84.0

You: Subtract 10 from that
Agent: The result is 74.0

You: Save that as answer
Agent: I've saved 74.0 as "answer" for you!

You: What's 100 minus 50?
Agent: 100 minus 50 equals 50.

You: What was answer?
Agent: Your saved value "answer" is 74.0.

You: history
Conversation History:
  - Added 25.0 + 17.0 = 42.0
  - Multiplied 42.0 × 2.0 = 84.0
  - Subtracted 10.0 from 84.0 = 74.0
  - Saved 74.0 as 'answer'
  - Subtracted 50.0 from 100.0 = 50.0
  - Recalled 'answer' = 74.0

You: saved
Saved Results:
  answer = 74.0

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
uv run pytest --cov=src
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
============================================================
TESTING CALCULATOR AGENT TOOLS
============================================================
Testing AddNumbersTool...
  ✅ 15.0 + 27.0 = 42.0
  ✅ Last result stored: 42.0

Testing MultiplyNumbersTool...
  ✅ 6.0 × 7.0 = 42.0

Testing SubtractNumbersTool...
  ✅ 10.0 - 3.0 = 7.0
  ✅ Last result stored: 7.0

Testing SaveResultTool and RecallResultTool...
  ✅ Saved 42.0 as 'my_number'
  ✅ 'my_number' = 42.0
  ✅ Correctly failed for non-existent result

Testing conversation flow...
  Step 1: 15.0 + 27.0 = 42.0
  Step 2: 42.0 × 3.0 = 126.0
  Step 3: Saved 126.0 as 'total'
  ✅ Conversation flow works correctly!

============================================================
✅ ALL TOOL TESTS PASSED!
============================================================
```

---

## 🛠️ Available Tools

The agent currently has **5 tools** available:

### 1. Add Numbers
**Usage:** "What's 5 plus 3?", "Add 10 and 20"
```python
AddNumbersTool(a, b) → a + b
```

### 2. Multiply Numbers
**Usage:** "Multiply 6 by 7", "What's 4 times 5?"
```python
MultiplyNumbersTool(a, b) → a × b
```

### 3. Subtract Numbers
**Usage:** "What's 50 minus 8?", "Subtract 10 from that"
```python
SubtractNumbersTool(a, b) → a - b
```

### 4. Save Result
**Usage:** "Save that as total", "Remember this as my_number"
```python
SaveResultTool(name, value) → Saves value with name
```

### 5. Recall Result
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
2. Future: We'll add SQLite/Redis for persistence

---

### "uv: command not found"

**Problem:** uv not installed or not in PATH

**Solution:**
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Restart terminal or reload shell
source ~/.bashrc  # or ~/.zshrc

# Verify
uv --version
```

---

## 📚 Learning Resources

### Understanding the Code

- **`main.py`** - Entry point, interactive loop
- **`src/calculator_agent/agents/calculator_agent.py`** - Main agent logic
- **`src/calculator_agent/tools/`** - Tool implementations
- **`src/calculator_agent/state/memory.py`** - State management

### Key Concepts

1. **Tool-based Architecture** - Each capability is a discrete tool
2. **Agent Loop** - Agent → Tool → Result → Response cycle
3. **State Management** - Memory shared across tools
4. **Type Safety** - Pydantic validates all data

### Documentation

- [Anthropic API Docs](https://docs.anthropic.com/)
- [LangChain Docs](https://python.langchain.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)

---

## 🔮 Future Enhancements

Planned features for future sessions:

- [ ] Division tool (with error handling)
- [ ] Power/exponent tool
- [ ] Square root tool
- [ ] Persistent storage (SQLite/Redis)
- [ ] Conversation history with full context
- [ ] Web API (FastAPI)
- [ ] Streaming responses
- [ ] Error recovery and retry logic
- [ ] Logging and debugging tools
- [ ] Multi-agent systems

---

## 📝 Development

### Adding New Tools

1. Create new tool class in `src/calculator_agent/tools/`:
```python
from .base import BaseTool
from ..models.schemas import MathOperationInput, ToolOutput

class DivideNumbersTool(BaseTool):
    def __init__(self, memory):
        self.memory = memory
    
    @property
    def name(self) -> str:
        return "divide_numbers"
    
    @property
    def description(self) -> str:
        return "Divide a by b. Returns a / b."
    
    def execute(self, input_data: MathOperationInput) -> ToolOutput:
        if input_data.b == 0:
            return ToolOutput(
                success=False,
                error="Division by zero",
                message="Cannot divide by zero"
            )
        
        result = input_data.a / input_data.b
        self.memory.set_last_result(result)
        self.memory.add_to_history(f"Divided {input_data.a} by {input_data.b} = {result}")
        
        return ToolOutput(
            success=True,
            result=result,
            message=f"{input_data.a} ÷ {input_data.b} = {result}"
        )
```

2. Register tool in `calculator_agent.py`:
```python
# Import
from ..tools.calculator import AddNumbersTool, MultiplyNumbersTool, SubtractNumbersTool, DivideNumbersTool

# Add to tools list
self.tools = [
    AddNumbersTool(self.memory),
    MultiplyNumbersTool(self.memory),
    SubtractNumbersTool(self.memory),
    DivideNumbersTool(self.memory),  # Add here
    # ...
]

# Update tool definitions
if tool.name in ["add_numbers", "multiply_numbers", "subtract_numbers", "divide_numbers"]:
    # ...

# Update input mapping
if tool.name in ["add_numbers", "multiply_numbers", "subtract_numbers", "divide_numbers"]:
    # ...
```

3. Add tests in `tests/test_tools.py`

---

## 📄 License

This is a learning project. Feel free to use and modify.

---

## 🙋 Support

If you encounter issues:

1. Check troubleshooting section above
2. Verify all prerequisites are installed
3. Test API connection with `scripts/verify_api.py`
4. Check `.env` file has valid API key

---

## ✅ Checklist: First Time Setup

- [ ] Python 3.11+ installed
- [ ] uv installed
- [ ] Project dependencies installed (`uv sync --all-extras`)
- [ ] `.env` file created with API key
- [ ] API test passes (`uv run python scripts/verify_api.py`)
- [ ] Agent runs successfully (`uv run python main.py`)

**If all checkboxes are ✅, you're ready to go!** 🚀

---

## 📊 Project Stats

**Current Status:**
- ✅ 5 tools implemented (add, multiply, subtract, save, recall)
- ✅ Full agent orchestration with Claude
- ✅ In-memory state management
- ✅ Type-safe with Pydantic
- ✅ Comprehensive tests
- ✅ Professional structure

**Next Up:**
- Division tool (with error handling)
- Power/exponent tool
- Better error handling
- Logging system

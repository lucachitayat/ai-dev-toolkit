# AI Developer Toolkit

An intelligent suite of AI-powered tools for streamlining software development workflows. Automate issue triage, code review, and more.

## What This Does

### Bug Triage (In Progress)
Automatically analyze GitHub issues and:
- Classify severity (critical, high, medium, low)
- Categorize by type (bug, feature, docs, etc.)
- Suggest priority level (P0-P4)
- Generate relevant labels
- Explain reasoning for decisions

### Code Review (Coming Soon)
- Security vulnerability detection
- Performance anti-patterns
- Code style suggestions
- Architecture recommendations

### More Tools Coming
- Documentation generation
- Test case generation
- SQL query optimization

## Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker & Docker Compose
- OpenAI API key
- `uv` (Python package manager) - [Install here](https://github.com/astral-sh/uv)

### Local Development Backend

```bash
# Clone repository
git clone https://github.com/lucachitayat/ai-dev-toolkit
cd ai-dev-toolkit

# Setup backend with uv
cd services/api
uv venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
uv sync --extra dev

# Run tests
pytest -v

# Start FastAPI server
python main.py
# API available at http://localhost:8081
# Swagger docs at http://localhost:8081/docs
```

### Quick Activate Alias (Optional)

Add to `~/.bashrc` for easy venv activation:

```bash
uv-activate() {
    local dir="$PWD"
    while [[ "$dir" != "/" ]]; do
        if [[ -f "$dir/.venv/bin/activate" ]]; then
            source "$dir/.venv/bin/activate"
            echo "✅ Activated venv from: $dir/.venv"
            return 0
        fi
        dir=$(dirname "$dir")
    done
    echo "❌ No .venv found"
    return 1
}
```

Then just run `uv-activate` from any subdirectory!

## Project Structure

```
ai-dev-toolkit/
├── services/                         # All application services
│   ├── api/                         # FastAPI backend
│   │   ├── .venv/                  # Virtual environment (uv)
│   │   ├── main.py                 # FastAPI app ✅
│   │   ├── schemas.py              # Pydantic validation schemas ✅
│   │   ├── models.py               # SQLAlchemy models ✅
│   │   ├── services/               # Business logic (coming soon)
│   │   ├── routes/                 # API endpoints (coming soon)
│   │   ├── tests/                  # pytest tests ✅
│   │   │   ├── test_schemas.py    # Schema validation tests (8 tests)
│   │   │   ├── test_models.py     # Model tests (5 tests)
│   │   │   ├── test_api.py        # API endpoint tests (1 test)
│   │   │   └── conftest.py        # pytest fixtures
│   │   ├── pyproject.toml          # uv dependencies
│   │   └── uv.lock                 # Lockfile
│   │
│   ├── frontend/                    # React dashboard (coming soon)
│   │   └── (Vite + React + Tailwind)
│   │
│   └── langgraph_agent/            # LangGraph AI pipeline (coming soon)
│       └── (OpenAI + LangChain integration)
│
├── resources/                       # Docker, configs, sample data
│   ├── docker-compose.yml          # (coming soon)
│   └── sample_data/                # Test data for triage
│
├── .gitignore                      # Git ignore patterns
├── CLAUDE.md                       # AI assistant guidance (dev only)
└── README.md                       # This file
```

**Current Status**: Day 1A complete - Schemas + Models + FastAPI (14 tests passing)

## API Endpoints

```
GET /health
├── Status: ✅ Implemented
└── Returns: { "status": "ok" }

POST /api/triage (coming soon)
├── Accepts: { title, body, labels?, author?, created_at? }
└── Returns: { severity, category, labels, priority, reasoning, confidence }

POST /github/webhook (coming soon)
├── GitHub issue webhook listener
└── Auto-comments with triage results
```

## Architecture

**Three-tier system:**
1. **Backend (FastAPI)**: REST API + async LLM orchestration
2. **Frontend (React)**: Interactive dashboard
3. **AI Pipeline (LangGraph)**: Single-call triage workflow

**Tech Stack:**
- **Backend**: FastAPI + SQLAlchemy (sync) + PostgreSQL + Pydantic
- **Frontend**: React + Vite + Tailwind CSS
- **AI**: LangGraph + OpenAI GPT-4o-mini (async)
- **Package Manager**: uv (faster than pip)
- **Testing**: pytest + pytest-asyncio (backend), Vitest (frontend)

**Key Design Choices:**
- Single LLM call with structured output (fast & cost-effective)
- Pydantic validation prevents invalid classifications
- FastAPI async endpoints (sync database for simplicity)
- GitHub webhook integration for production use
- Strict TDD discipline (RED-GREEN-REFACTOR cycle)

## Testing

```bash
# Backend tests (TDD approach)
cd services/api
source .venv/bin/activate  # or use uv-activate
pytest -v                   # All tests
pytest tests/test_schemas.py -v  # Specific file

# Frontend tests (coming soon)
cd services/frontend
npm run test
```

**Current Test Coverage:**
- [x] Pydantic schema validation (8 tests passing)
  - IssueInput: required fields, optional fields, defaults, missing fields
  - TriageDecision: enum validation, confidence range validation
- [x] SQLAlchemy models (5 tests passing)
  - Triage model: creation, constraints, field assignment, auto-generated IDs
- [x] FastAPI endpoints (1 test passing)
  - Health check endpoint
- [ ] LLM integration (coming soon)
- [ ] Triage service (coming soon)

## Development Philosophy

This project follows **Test-Driven Development (TDD)**:
1. **RED**: Write failing test
2. **GREEN**: Write minimal code to pass
3. **REFACTOR**: Improve code while keeping tests green

All features are tested before implementation.

## Deployment

### Deploy to Production

```bash
# Build Docker images
docker-compose -f resources/docker-compose.yml build

# Push to registry
docker push your-registry/ai-toolkit-api:latest

# Deploy (Kubernetes, Heroku, etc.)
```

## Documentation

- [Architecture Deep Dive](./docs/ARCHITECTURE.md)
- [API Reference](./docs/API.md)
- [Development Guide](./docs/DEVELOPMENT.md)
- [GitHub App Setup](./docs/GITHUB_APP_SETUP.md)

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

MIT

## Questions?

Open an issue or check the [FAQ](./docs/FAQ.md).

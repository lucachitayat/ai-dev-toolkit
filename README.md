# AI Developer Toolkit

An intelligent suite of AI-powered tools for streamlining software development workflows. Automate issue triage, code review, and more.

## 🎯 What This Does

### Bug Triage (Now)
Automatically analyze GitHub issues and:
- 🏷️ Classify severity (critical, high, medium, low)
- 📂 Categorize by type (bug, feature, docs, etc.)
- 🎯 Suggest priority level (P0-P4)
- 🔖 Generate relevant labels
- 🤖 Explain reasoning for decisions

### Code Review (Coming Soon)
- Security vulnerability detection
- Performance anti-patterns
- Code style suggestions
- Architecture recommendations

### More Tools Coming
- Documentation generation
- Test case generation
- SQL query optimization

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- OpenAI API key

### Local Development (5 minutes)

```bash
# Clone and setup
git clone <repo>
cd ai-dev-toolkit

# Setup backend
cd project/api
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
pytest

# Setup frontend
cd ../frontend
npm install
npm run dev

# Start with Docker Compose (all services)
cd ../../resources
docker-compose up --build
```

Visit `http://localhost:5173` to see the dashboard.

## 📊 Project Structure

```
project/
├── api/                          # Flask REST API
│   ├── app.py                   # Application factory
│   ├── models.py                # Database models
│   ├── config.py                # Environment config
│   ├── requirements.txt
│   ├── tests/
│   └── conftest.py
│
├── frontend/                     # React dashboard
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── utils/               # Helpers (API client, formatters)
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── langgraph_agent/             # LangGraph AI pipeline
    ├── main.py                  # Orchestration
    ├── graph/
    │   ├── state.py            # State definition
    │   ├── nodes.py            # Workflow nodes
    │   └── workflow.py         # Graph assembly
    ├── services/
    │   ├── api_client.py       # HTTP client
    │   └── llm_service.py      # LLM integration
    └── utils/
        └── json_loader.py      # Data parsing
```

## 🔌 API Endpoints

```
POST /api/triage
├── Accepts: { title, description, repo_context? }
└── Returns: { severity, category, labels, priority, reasoning }

POST /github/webhook
├── GitHub issue webhook listener
└── Auto-comments with triage results

GET /health
└── Health check endpoint
```

## 🏗️ Architecture

**Three-tier system:**
1. **Backend (Flask)**: REST API + LLM orchestration
2. **Frontend (React)**: Interactive dashboard
3. **AI Pipeline (LangGraph)**: Multi-step reasoning workflows

**Key Design Choices:**
- Single LLM call with structured output (fast & cost-effective)
- Pydantic validation prevents invalid classifications
- GitHub webhook integration for production use
- TDD discipline throughout

## 🧪 Testing

```bash
# Backend tests
cd project/api
pytest -v

# Frontend tests
cd project/frontend
npm run test

# Run all tests
cd ../..
./scripts/test-all.sh
```

## 📝 Development Philosophy

This project follows **Test-Driven Development (TDD)**:
1. 🔴 Write failing test
2. 🟢 Write minimal code to pass
3. ♻️ Refactor while keeping tests green

All features are tested before implementation.

## 🚢 Deployment

### Deploy to Production

```bash
# Build Docker images
docker-compose -f resources/docker-compose.yml build

# Push to registry
docker push your-registry/ai-toolkit-api:latest

# Deploy (Kubernetes, Heroku, etc.)
```

## 📚 Documentation

- [Architecture Deep Dive](./docs/ARCHITECTURE.md)
- [API Reference](./docs/API.md)
- [Development Guide](./docs/DEVELOPMENT.md)
- [GitHub App Setup](./docs/GITHUB_APP_SETUP.md)

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 📄 License

MIT

## 🙋 Questions?

Open an issue or check the [FAQ](./docs/FAQ.md).

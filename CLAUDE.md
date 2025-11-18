# CLAUDE.md - AI Developer Toolkit

**Last Updated**: 2025-11-17 (22:18 UTC)  
**Project Start**: 2025-11-14  
**Target Completion**: 2025-11-24 (10 days, flexible)  
**Status**: Day 1A: Complete (14 tests passing) - Schemas + Models + FastAPI

---

## IMPORTANT: This is a Learning Project

**How Claude Should Interact:**

This project is designed as a **learning vehicle**, not just to ship code. Claude's role is to:

1. **Explain the "why" behind every decision**
   - Don't just write code; explain architectural choices
   - Show trade-offs between options
   - Help understand best practices

2. **Guide, don't implement**
   - Ask guiding questions before writing code
   - Encourage thinking about design before coding
   - Point out conventions and patterns, let you discover them

3. **Encourage TDD discipline (Pure Red-Green-Refactor)**
   - Write failing test first (RED)
   - Write minimal code to pass (GREEN)
   - Refactor while keeping tests green (REFACTOR)
   - This is strict TDD for learning best practices

4. **Document decisions in CLAUDE.md**
   - Update this file regularly with decisions and reasoning
   - Capture "why" we chose something
   - Help with context switching between sessions

5. **Provide just-in-time learning**
   - Teach async/await when we need it
   - Explain type hints as they appear
   - Don't overwhelm with unused information

**What Claude should NOT do:**
- Write complete files without explanation
- Skip the reasoning behind decisions
- Assume prior knowledge (ask first)
- Add features not explicitly requested
- Create files without user understanding why
- **Use emojis in documentation** (looks AI-generated, unprofessional)

**Teaching Style (Decided)**:
- **First encounter**: Explain thoroughly (compare to C#/TypeScript where relevant)
- **Subsequent uses**: Trust understanding, only highlight differences
- **Example**: First `@app.post()` decorator -> full explanation. Second one -> assume you got it

---

## 🎯 Project Vision

Build a **hybrid AI Developer Toolkit** - a suite of AI-powered tools that help developers automate repetitive tasks and make better decisions. Think of it as Copilot for your entire development workflow.

**Why this project?**
- ✅ More interesting than IHX for GitHub portfolio
- ✅ Broader appeal (every developer relates to the problems)
- ✅ Can be built incrementally (MVP in 5 days)
- ✅ Clear monetization path (B2B SaaS potential)
- ✅ Reuses tech stack you already know (Flask, React, LangGraph)

---

## 📊 Project Scope

### Phase 1: Bug Triage (Days 1-3, Completed by Day 5)
**Problem**: Open-source maintainers and PM teams drown in GitHub issues. No clear prioritization.

**Solution**: AI automatically analyzes issues and suggests:
- Severity classification (critical → low)
- Category detection (bug vs feature vs docs)
- Priority level (P0 → P4)
- Label suggestions (backend, frontend, security, etc.)
- Reasoning explanation (why this priority?)

**Output**: Auto-comment on GitHub issues with triage results + apply labels

**Success Metrics**:
- ✅ Works on real GitHub issues
- ✅ Accuracy > 80% (human reviewers agree with categorization)
- ✅ Deployable as GitHub app

### Phase 2: Code Review (Days 6-7, added after Phase 1)
**Problem**: Manual code reviews miss security issues and performance problems.

**Solution**: AI analyzes pull requests for:
- Security vulnerabilities (SQL injection, XSS, etc.)
- Performance anti-patterns (N+1 queries, inefficient loops)
- Code style violations (linting)
- Architecture suggestions

**Output**: Comments on PRs with specific issues + learning resources

### Phase 3: Other Tools (Optional, Beyond 5 Days)
- Documentation generator (auto-generate README from code)
- Test case generator (suggest tests for new functions)
- SQL query optimizer (suggest indexes, rewrites)

---

## 🏗️ Technical Architecture

### Tech Stack
- **Backend**: FastAPI + SQLAlchemy (sync) + PostgreSQL
- **Frontend**: React + Vite + Tailwind CSS
- **AI Pipeline**: LangGraph + OpenAI GPT-4o-mini (async)
- **Infrastructure**: Docker Compose (4 services)
- **Testing**: pytest + pytest-asyncio (backend), Vitest (frontend)
- **Package Manager**: uv (faster than pip)
- **Dependency Management**: pyproject.toml (modern Python standard)

### Why These Choices?
1. **FastAPI over Flask**: Interview preparation (next role wants FastAPI), async/await patterns, better performance, built-in validation + docs
2. **C# async/await background**: Easy transition to Python async (same concept)
3. **Bug triage is simpler than IHX**: 1 LLM call, good learning project for async patterns
4. **uv + pyproject.toml**: Modern Python tooling, faster than pip, industry standard
5. **TDD**: Familiar testing patterns from IHX

### Key Design Decisions

#### 1. Single LLM Call (Not Multi-Step Workflow)
**IHX had**: 5-node LangGraph (load → extract → analyze → create → decide)  
**Bug Triage has**: 1-node workflow (classify issue in one go)

```python
# Pseudocode
prompt = f"""
Issue Title: {issue.title}
Issue Body: {issue.body}

Classify this GitHub issue:
1. Severity: critical | high | medium | low
2. Category: bug | feature | docs | refactor | chore
3. Priority: P0 | P1 | P2 | P3 | P4
4. Labels: [array of suggested labels]
5. Reasoning: Brief explanation

Return as JSON.
"""

response = llm.call_structured(prompt, schema=TriageDecision)
```

**Why simpler?**: Classification is deterministic, doesn't need reasoning chain

#### 2. Pydantic Structured Output
```python
class TriageDecision(BaseModel):
    severity: Literal["critical", "high", "medium", "low"]
    category: Literal["bug", "feature", "docs", "refactor", "chore"]
    priority: Literal["P0", "P1", "P2", "P3", "P4"]
    labels: List[str]
    reasoning: str
```

**Why?**: Prevents LLM hallucination, ensures valid classifications

#### 3. GitHub Webhook Integration
```
GitHub Issue Created
    ↓
POST /github/webhook
    ↓
Validate signature
    ↓
Call /api/triage
    ↓
Post comment + apply labels
    ↓
Done
```

**Why?**: Makes it *actually useful* (automatic, not manual)

#### 4. Simple Database
```python
class Triage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_url = db.Column(db.String, unique=True)
    title = db.Column(db.String)
    severity = db.Column(db.String)
    category = db.Column(db.String)
    priority = db.Column(db.String)
    labels = db.Column(db.JSON)
    reasoning = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
```

**Why?**: Track decisions for analytics + debugging

---

## 📅 10-Day Learning Plan (Flexible Milestones)

**Philosophy**: Focus on understanding, not speed. Each milestone should be solid and tested before moving forward.

---

### Days 1-2: Core API Foundation

#### Day 1A: Schemas + Models + FastAPI Basics (✅ COMPLETE)

**Goal**: Understand Pydantic validation, SQLAlchemy models, FastAPI basics

**Tasks**:
- [x] Setup uv venv + pyproject.toml
- [x] Create Pydantic schemas (`schemas.py`)
  - IssueInput schema (request validation)
  - TriageDecision schema (LLM output)
- [x] Create SQLAlchemy models (`models.py`)
  - Triage table (sync database)
- [x] Basic FastAPI app (`main.py`)
  - Health check endpoint
  - Uvicorn server configuration
- [x] Write tests for schemas, models, and API

**Learning Focus**: Type hints, Pydantic validation, SQLAlchemy ORM, FastAPI basics

**Acceptance Criteria**:
- ✅ Pydantic schemas validate input correctly (8 tests)
- ✅ Can create Triage record in database (5 tests)
- ✅ FastAPI health endpoint works (1 test)
- ✅ All 14 tests pass
- ✅ FastAPI app runs: `python main.py`

---

#### Day 1B: LLM Service + Triage Logic (🔵 NEXT)

**Goal**: Integrate OpenAI, understand async patterns

**Estimated Time**: 1-2 hours

---

##### Task 1: LLM Service (Async OpenAI Integration)
**File**: `services/llm_service.py`

**What to Build**:
- Async OpenAI client wrapper
- Structured output using Pydantic `TriageDecision`
- System prompt for triage classification
- Error handling (API failures, rate limits)

**Tests** (`tests/test_llm_service.py`):
1. Successful triage classification (mocked LLM response)
2. Handles invalid LLM output (schema validation)
3. Handles OpenAI API errors (network failures)
4. System prompt includes severity/category/priority guidelines

**Key Concepts to Learn**:
- `async`/`await` in Python (event loop vs threads)
- OpenAI SDK (ChatCompletion API)
- Structured outputs with Pydantic
- Mocking async functions in pytest

**TDD Flow**:
1. Write test for successful classification (mocked response)
2. Implement minimal `classify_issue()` function
3. Write test for invalid LLM output
4. Add validation error handling
5. Write test for API errors
6. Add error handling

---

##### Task 2: Triage Service (Business Logic Layer)
**File**: `services/triage_service.py`

**What to Build**:
- `async def triage_issue(issue_input: IssueInput) -> TriageDecision`
- Call LLM service
- Save result to database (sync SQLAlchemy)
- Return decision

**Tests** (`tests/test_triage_service.py`):
1. End-to-end: Input → LLM → Database → Output
2. Prevents duplicate triages (unique `issue_url`)
3. Handles LLM service failures gracefully

**Key Concepts**:
- Mixing async (LLM) with sync (database)
- Service layer pattern (separation of concerns)
- Integration testing strategy

**TDD Flow**:
1. Write test for full triage flow (mocked LLM)
2. Implement `triage_issue()` function
3. Write test for duplicate prevention
4. Add uniqueness check
5. Write test for LLM failure handling
6. Add error handling

---

##### Dependencies to Add

```toml
[project]
dependencies = [
    "fastapi>=0.121.0",
    "uvicorn>=0.38.0",
    "sqlalchemy>=2.0.0",
    "pydantic>=2.0.0",
    "openai>=1.0.0",        # NEW
    "python-dotenv>=1.0.0", # NEW
]
```

---

##### Environment Setup

**Before starting:**

```bash
# Create .env file
echo "OPENAI_API_KEY=your-key-here" > .env

# Add to .gitignore
echo ".env" >> .gitignore

# Install dependencies
uv sync
```

---

##### File Structure After Day 1B

```
services/api/
├── main.py
├── schemas.py
├── models.py
├── services/
│   ├── __init__.py
│   ├── llm_service.py      # NEW
│   └── triage_service.py   # NEW
├── tests/
│   ├── conftest.py
│   ├── test_schemas.py     (8 tests)
│   ├── test_models.py      (5 tests)
│   ├── test_api.py         (1 test)
│   ├── test_llm_service.py     # NEW (~4 tests)
│   └── test_triage_service.py  # NEW (~3 tests)
├── .env                    # NEW (gitignored)
└── pyproject.toml
```

**Expected Test Count**: ~21 tests passing

---

**Learning Focus**: Async/await fundamentals, OpenAI SDK, mocking in tests

**Acceptance Criteria**:
- [ ] LLM service returns valid TriageDecision
- [ ] Triage service saves to database
- [ ] All tests pass with mocked LLM responses
- [ ] ~21 tests passing total
- [ ] No real OpenAI API calls in tests (all mocked)

---

#### Day 2: POST /api/triage Endpoint + Comprehensive Tests

**Goal**: Complete end-to-end triage flow

**Tasks**:
- [ ] Create `/api/triage` endpoint
  - Accepts IssueInput
  - Calls triage service
  - Returns TriageDecision
- [ ] Error handling (invalid input, LLM failures)
- [ ] Integration tests (full flow)
- [ ] Manual testing with curl

**Learning Focus**: FastAPI routing, error handling, integration testing

**Acceptance Criteria**:
- ✅ POST /api/triage works end-to-end
- ✅ Returns valid JSON
- ✅ Handles errors gracefully
- ✅ All tests pass (unit + integration)

---

### Days 3-4: GitHub Integration

#### Day 3: Webhook Listener + Signature Validation

**Goal**: Understand GitHub webhooks, API authentication

**Tasks**:
- [ ] Create webhook endpoint (`POST /github/webhook`)
- [ ] Implement GitHub signature validation
- [ ] Parse GitHub issue event payload
- [ ] Write tests with sample webhook payloads

**Learning Focus**: Webhooks, HMAC signature validation, GitHub API

---

#### Day 4: GitHub API Client + Auto-Commenting

**Goal**: Complete GitHub integration

**Tasks**:
- [ ] Create GitHub API client (`services/github_client.py`)
- [ ] Implement comment posting
- [ ] Implement label application
- [ ] Wire webhook → triage → GitHub flow
- [ ] Test on real GitHub repo

**Learning Focus**: REST API integration, authentication, error handling

**Acceptance Criteria**:
- ✅ Webhook triggers triage
- ✅ Comments posted to GitHub issues
- ✅ Labels applied correctly
- ✅ Works on test repository

---

### Days 5-6: React Dashboard

#### Day 5: React Setup + Form Component

**Goal**: Setup React, create input form, connect to API

**Tasks**:
- [ ] Initialize Vite + React project
- [ ] Setup Tailwind CSS
- [ ] Create IssueTriageForm component
- [ ] Create API client (axios)
- [ ] Test form submission to backend

**Learning Focus**: React hooks, API integration, form handling

---

#### Day 6: Results Display + History

**Goal**: Display results, show history, polish UI

**Tasks**:
- [ ] Create TriageResult component
- [ ] Create RecentTriages table component
- [ ] Add formatters (severity badges, etc.)
- [ ] Component tests (Vitest)
- [ ] Polish styling

**Learning Focus**: Component composition, state management, testing

**Acceptance Criteria**:
- ✅ Results display beautifully
- ✅ History table shows past triages
- ✅ Professional look and feel
- ✅ Component tests pass

---

### Days 7-8: Polish + Infrastructure

#### Day 7: Docker Compose + Configuration

**Goal**: Make it deployable

**Tasks**:
- [ ] Create docker-compose.yml
- [ ] Dockerfiles for api + frontend
- [ ] Environment variable configuration
- [ ] Database persistence (volumes)
- [ ] One-command setup script

**Learning Focus**: Docker, containerization, configuration management

---

#### Day 8: Error Handling + Logging + Validation

**Goal**: Production-ready error handling and observability

**Tasks**:
- [ ] Comprehensive error handling (all endpoints)
- [ ] Structured logging (not just print statements)
- [ ] Input validation improvements
- [ ] Graceful LLM failure handling
- [ ] User-friendly error messages

**Learning Focus**: Production best practices, debugging, observability

---

### Days 9-10: Documentation + Demo

#### Day 9: Documentation

**Goal**: Clear documentation for portfolio

**Tasks**:
- [ ] README with quick start
- [ ] ARCHITECTURE.md (system design)
- [ ] API.md (endpoint reference)
- [ ] GITHUB_APP_SETUP.md (installation guide)
- [ ] Code comments and docstrings

**Learning Focus**: Technical writing, documentation best practices

---

#### Day 10: Demo + GitHub App Publishing

**Goal**: Portfolio-ready launch

**Tasks**:
- [ ] Record demo video (60-90 seconds)
- [ ] Publish as GitHub app
- [ ] Create example repository
- [ ] Setup CI/CD (.github/workflows/tests.yml)
- [ ] Final testing and polish

**Acceptance Criteria**:
- ✅ Demo video showcases full workflow
- ✅ GitHub app installable and working
- ✅ Documentation is clear and complete
- ✅ CI/CD tests passing
- ✅ Portfolio-ready

---

## 🔄 Decision Log (Session-by-Session)

### Planning Session Decisions (2025-11-14)

**1. Database: Sync vs Async SQLAlchemy**
- ✅ DECISION: Use **Sync SQLAlchemy** for Day 1
- Reasoning:
  - More practical (70%+ of FastAPI production code uses sync)
  - Faster to implement (familiar from IHX)
  - Shows good engineering judgment (async where it matters: LLM calls)
  - Can upgrade to async later if needed
- Interview story: "Used async for LLM calls where I/O latency matters, kept database sync for simplicity"

---

## 🔄 Daily Progress Log

### Day 1A Session 1: Basic Schemas + Testing Setup (2025-11-14 22:17 UTC) ✅ COMPLETE

**Completed:**
- ✅ Setup uv venv in `services/api/`
- ✅ Created `pyproject.toml` with proper dependencies
- ✅ Installed pytest + pytest-asyncio + ruff
- ✅ Created basic `schemas.py` with Pydantic models:
  - `IssueInput` (request validation)
  - `TriageDecision` (LLM output structure)
- ✅ Wrote 3 tests following TDD (RED → GREEN)
- ✅ All tests passing

**Dependencies Added:**
- `pydantic>=2.0.0` (validation)
- `pytest>=7.4.0` (testing)
- `pytest-asyncio>=0.21.0` (async test support)
- `ruff>=0.1.0` (linting + formatting)

**Key Learnings:**
- TDD cycle: Write failing test first → See red → Implement minimal code → See green
- Pydantic `BaseModel` provides automatic validation
- Type hints = validation rules (`title: str` means required string)
- `pytest.raises(ValidationError) as exc_info` pattern for validation testing
- Python import gotcha: Created `schemas/schemas.py` by mistake, fixed to `schemas.py`

**Key Decisions:**
- Using `pyproject.toml` for dependency management (modern Python standard)
- Testing error messages by checking field name (resilient to Pydantic version changes)
- Docstrings on tests for clarity

---

### Day 1A Session 2: Enhanced Schemas with Validation (2025-11-15 02:52 UTC) ✅ COMPLETE

**Completed:**
- ✅ Enhanced `IssueInput` schema:
  - Renamed `description` → `body` (matches GitHub API)
  - Added optional fields: `labels` (default `[]`), `author`, `created_at`
  - Used modern Python syntax: `str | None` instead of `Optional[str]`
- ✅ Enhanced `TriageDecision` schema:
  - Added `Literal` types for `severity`, `category`, `priority` (enum validation)
  - Added `confidence: float` field with `Field(ge=0.0, le=1.0)` range constraint
- ✅ Expanded test coverage to 8 tests (all passing in 0.18s):
  - 4 tests for `IssueInput` (required fields, optional defaults, missing title/body)
  - 4 tests for `TriageDecision` (invalid severity/category/priority, invalid confidence)
- ✅ Setup pytest-watcher with config file for hot reload
- ✅ Configured WSL + Windows dual development environment
- ✅ Fetched latest docs for Pydantic, FastAPI, pytest via Context7

**Development Environment Improvements:**
- Created `.pytest-watcher.yaml` for efficient test watching
- Resolved WSL filesystem performance issues (moved to Windows for faster execution)
- Configured Cursor with Python interpreter for proper IntelliSense
- Established workflow: Windows for development, WSL for commands

**Key Learnings:**
- `Literal["val1", "val2"]` for enum-like validation (modern alternative to Enum)
- `Field(ge=, le=)` for numeric range constraints
- Modern union syntax `str | None` preferred over `Optional[str]` in Python 3.10+
- pytest-watcher requires ignoring `.venv` directory to avoid noise
- WSL filesystem (`/mnt/c/`) is slower than native Windows for file operations
- `pyproject.toml` separates direct dependencies from transitive (cleaner than requirements.txt)

**Key Decisions:**
- Use `Literal` types instead of Enum classes (simpler, recommended by Pydantic v2)
- Keep `body` field name to match GitHub API (not `description`)
- Add `confidence` score for LLM output validation
- Use pytest-watcher for development (hot reload tests)
- Work from Windows filesystem for better performance

**Blocked:** None

**Next:** SQLAlchemy models with TDD (database layer)

---

### Day 1A Session 3: SQLAlchemy Models with TDD (2025-11-16 23:33 UTC) ✅ COMPLETE

(Content remains the same)

---

### Day 1A Session 4: FastAPI Basics with Health Endpoint (2025-11-17 22:18 UTC) ✅ COMPLETE

**Completed:**
- ✅ Created `models.py` with `Triage` model:
  - All required fields (issue_url, title, body, severity, category, priority, labels, reasoning, confidence)
  - Auto-generated fields (id, created_at)
  - Unique constraint on `issue_url`
  - Proper nullable constraints
- ✅ Created `conftest.py` with `db_session` fixture:
  - SQLite in-memory database for tests
  - Automatic table creation/cleanup
  - Follows pytest fixture pattern
- ✅ Added 5 comprehensive model tests (all passing):
  - Model creation with all fields
  - Unique constraint enforcement (issue_url)
  - Field assignment validation
  - Auto-generated ID uniqueness
  - ID conflict detection
- ✅ Fetched SQLAlchemy 2.0 docs via Context7 for best practices

**Dependencies Added:**
- `sqlalchemy>=2.0.0` (ORM)

**Key Learnings:**
- SQLAlchemy 2.0 uses `declarative_base()` from `sqlalchemy.orm` (not `sqlalchemy.ext.declarative`)
- `__tablename__` is required for every model
- Lambda functions for `default=` ensure values are computed per-record (not once at class definition)
- SQLite in-memory (`sqlite:///:memory:`) is fast for unit tests, but doesn't enforce all constraints
- `IntegrityError` is raised for unique constraint violations
- Fixtures use `yield` for setup/teardown pattern
- xUnit setup/teardown pattern = pytest fixtures (more flexible)

**Key Decisions:**
- Use SQLite for unit tests (fast, no setup), reserve PostgreSQL for integration tests
- Use `lambda: datetime.now(timezone.utc)` for created_at default (timezone-aware)
- Test field assignment rather than NULL constraint enforcement (SQLite limitation)
- Use `IntegrityError` (not generic `Exception`) for constraint tests
- Suppress `SAWarning` about identity conflicts in tests (expected behavior)

**Blocked:** None

**Next:** FastAPI basics (health check endpoint)

---

## 🔄 Daily Standup Template (Keep CLAUDE.md Updated)

**At the end of each day**, update this section:

### Day 1 Status
- [ ] What was completed
- [ ] What was attempted but blocked
- [ ] What's next
- [ ] Key learnings/decisions made

**Example:**
```
### Day 1: API + LLM Core ✅ COMPLETE
- ✅ Flask app factory working (copied from IHX)
- ✅ OpenAI integration via LangGraph (single call)
- ✅ Pydantic TriageDecision schema defined
- ✅ POST /api/triage returns valid JSON
- ✅ 8 pytest tests (all green)
- ❌ Blocked: None
- 🎯 Next: GitHub webhook integration

Key Decisions:
- Used single LLM call (not multi-step) to keep it simple
- Reused IHX's LLMService pattern verbatim
- Added TriageDecision Pydantic model for validation
```

---

## 💡 Key Implementation Details

### System Prompt for Triage

```python
TRIAGE_SYSTEM_PROMPT = """
You are an expert GitHub issue classifier. Analyze issues and categorize them.

SEVERITY GUIDELINES:
- Critical: Breaks production, data loss, security breach
- High: Major feature broken, significant performance impact
- Medium: Minor feature broken, inconvenience, cosmetic issues
- Low: Documentation, typos, future improvements

CATEGORY GUIDELINES:
- bug: Something is broken
- feature: New functionality request
- docs: Documentation improvements
- refactor: Code quality improvements
- chore: Maintenance tasks (deps, tooling, etc.)

PRIORITY GUIDELINES:
- P0: Fix immediately (production down)
- P1: Fix this sprint (blocking other work)
- P2: Fix soon (affects users)
- P3: Fix when possible (nice to have)
- P4: Backlog (maybe never)

LABELS GUIDELINES:
Suggest 2-3 relevant labels from:
- bug, feature, docs, refactor, chore
- backend, frontend, database, devops, ci-cd
- security, performance, accessibility, testing
- help-wanted, good-first-issue, discussion, blocked
"""
```

### Deployment

**To GitHub App**:
```bash
# 1. Register at https://github.com/settings/apps
# 2. Set webhook URL to deployed API
# 3. Give permissions: issues (read/write), repo contents (read)
# 4. Install on test repo
# 5. Create test issue → should auto-comment
```

**To Heroku/Railway/Fly.io**:
```bash
docker-compose build
docker push your-registry/ai-toolkit-api:latest
# Deploy via platform's dashboard
```

---

## 🎓 Learning from IHX

**What worked well:**
- ✅ Application Factory pattern (easy testing)
- ✅ LangGraph structured output (prevents bad LLM responses)
- ✅ Docker Compose (local dev matches production)
- ✅ TDD approach (caught bugs early)
- ✅ Pydantic validation (clean error messages)

**What to improve in this project:**
- Input validation on all endpoints (add earlier)
- Pagination from day 1 (not day 5)
- Better error messages for LLM failures
- Logging from the start (helps debugging)

---

## 🚀 Velocity Assumptions

**Why 5 days is realistic:**

| Task | Estimated Time | Reasoning |
|------|---|---|
| Flask API scaffold | 2 hours | Copy IHX patterns |
| LLM integration | 1 hour | Reuse LLMService |
| Pydantic models | 1 hour | Similar to IHX |
| GitHub integration | 3 hours | New but straightforward |
| React UI | 3 hours | Similar to IHX frontend |
| Docker setup | 2 hours | Reuse docker-compose |
| Documentation | 3 hours | Must be good |
| Testing | 5 hours | TDD throughout |
| Buffer/Polish | 3 hours | Unexpected issues |
| **Total** | **~24 hours** | **~5 days (8 hrs/day)** |

---

## 📋 Immediate Next Steps

**Right now:**
1. ✅ Create project folder structure
2. ✅ Write CLAUDE.md (this file!)
3. ✅ Create README.md
4. 🎯 **Start Day 1: API + LLM Core**

**Start with**:
```bash
cd project/api
python -m venv venv
source venv/bin/activate
pip install flask sqlalchemy python-dotenv openai langchain langgraph pydantic pytest
```

---

## 🔮 Future Upgrades (Post-MVP)

**Potential improvements after Day 5:**

1. **Async SQLAlchemy** (Performance)
   - Upgrade from sync to async database
   - Non-blocking database I/O
   - Better for high-concurrency scenarios
   - Estimated effort: 4-6 hours

2. **Caching Layer** (Redis)
   - Cache triage results for duplicate issues
   - Reduce LLM API costs
   - Faster response times

3. **Rate Limiting** (Production)
   - Prevent abuse of triage endpoint
   - Per-user/per-IP limits

4. **Monitoring** (Observability)
   - Prometheus metrics
   - Sentry error tracking
   - OpenTelemetry tracing

5. **Multi-LLM Support**
   - Add Anthropic Claude, Llama, etc.
   - A/B test accuracy across models
   - Fallback if OpenAI is down

---

## 🤔 Decision Log

### Planning Session Decisions (2025-11-14 21:20 UTC)

**1. Database: Sync vs Async SQLAlchemy**
- ✅ DECISION: Use **Sync SQLAlchemy** for MVP
- Reasoning:
  - More practical (70%+ of production FastAPI uses sync)
  - Faster to implement (familiar from IHX)
  - Shows good engineering judgment (async where it matters: LLM)
  - Can upgrade to async later (see Future Upgrades)
- Interview story: "Used async for LLM calls where I/O latency matters, kept database sync for simplicity and maintainability"

**2. Folder Structure**
- ✅ DECISION: Use `services/` (not `project/`)
- Reasoning: Multi-service architecture, clearer naming
- All references in CLAUDE.md updated to reflect actual structure

**3. Timeline**
- ✅ DECISION: 10-day flexible learning plan (not 5-day sprint)
- Reasoning: Focus on understanding over speed, time for experimentation
- Each milestone should be solid before moving forward

**4. Learning Style**
- ✅ DECISION: "Explain first time, trust after that"
- First encounter: Full explanation with C#/TypeScript comparisons
- Subsequent uses: Assume understanding, only highlight differences

**5. Code Style**
- ✅ Type hints: Everywhere (modern Python standard)
- ✅ Docstrings: On complex/non-obvious functions (industry standard)
- ✅ Skip docstrings: On trivial helpers (avoid noise)
- Reasoning: Follow Google Python Style Guide, prepare for interviews

**6. Testing Strategy**
- DECISION: Pure TDD (Red-Green-Refactor cycle)
- Write test first → See it fail (RED) → Implement minimal code → See it pass (GREEN) → Refactor (REFACTOR)
- Reasoning: Learn TDD discipline from ground-up, industry best practice, safer refactoring
- Benefits: Think about interface first, prevent over-engineering, confidence in code
- Example flow:
  ```python
  # 1. RED: Write failing test
  def test_classify_issue():
      result = classify_issue(issue)
      assert result.severity == "high"  # ❌ Function doesn't exist
  
  # 2. GREEN: Minimal implementation
  def classify_issue(issue):
      return TriageDecision(severity="high")  # ✅ Hardcoded passes
  
  # 3. REFACTOR: Real implementation
  def classify_issue(issue):
      return llm_service.call(issue)  # ✅ Still passes, now real
  ```

**Original planning decisions:**

1. **Why hybrid toolkit instead of single tool?**
   - Answer: Larger portfolio impact, can build incrementally, shows breadth

2. **Why bug triage first?**
   - Answer: Simpler than code review, most relatable problem, can launch in 3 days

3. **Why single LLM call instead of multi-step?**
   - Answer: Classification is deterministic, faster, cheaper, simpler

4. **Why GitHub webhook integration?**
   - Answer: Makes it actually useful (automatic), impressive for demo

5. **Why not add auth/security from day 1?**
   - Answer: Scope creep, MVP first, can add later if needed

---

## 🔗 Related Documents

- `README.md` - Quick start and overview
- `project/api/tests/` - Test files
- `project/frontend/src/` - React components
- `.env.example` - Environment variables

---

## ⚡ Quick Reference Commands

```bash
# Setup
cd project/api && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run tests
pytest -v                           # All tests
pytest -k "test_name"              # Specific test
pytest --cov                       # With coverage

# Run locally
python app.py                      # Starts on port 8081

# Frontend
cd project/frontend
npm install
npm run dev                        # Starts on port 5173

# Docker
cd resources && docker-compose up --build

# Verify
curl http://localhost:8081/health
curl -X POST http://localhost:8081/api/triage -d '{"title":"test","description":"test"}'
```

---

**7. Git Workflow and Clean History**
- DECISION: Clean linear history for portfolio presentation
- Branches: `master` (production, default), `develop` (integration), `feature/*` (work)
- Use interactive rebase to maintain clean history before merging
- Atomic commits: one logical change per commit
- Professional commit messages with clear format
- Never rebase public/shared commits (only local work)

**Git Strategy Details** (for portfolio projects):

1. **Atomic Commits**: Each commit represents one complete, logical change
   - Self-contained (doesn't break the build)
   - Single purpose (not mixing unrelated changes)
   - Clear message explaining what and why

2. **Commit Message Format**:
   ```
   <Action> <feature> <with details>
   
   - Bullet point of implementation
   - Bullet point of technical decisions
   - Bullet point of test coverage
   
   Tech: <technologies>
   Tests: X/X passing
   ```

3. **Interactive Rebase Workflow**:
   ```bash
   # Squash messy commits before pushing
   git rebase -i HEAD~N
   
   # Commands:
   pick   = keep commit as-is
   squash = combine with previous commit
   reword = edit commit message
   drop   = remove commit
   ```

4. **When to Rebase**:
   - ✅ Before pushing to clean up local commits
   - ✅ Before creating PR to present clean history
   - ✅ To catch up with main branch changes
   - ❌ Never on shared/public commits (breaks others' work)

5. **Maximizing GitHub Contributions**:
   - Commit frequency: After each test pass or feature completion
   - Push at end of each session (shows activity)
   - Consistent daily commits during active development
   - Quality commits > quantity, but consistency matters for employer visibility

**Example Clean History** (this project):
```
* Fix .gitignore line endings
* Update documentation for Day 1A completion
* Add FastAPI application with health check endpoint
* Add SQLAlchemy models with database layer
* Add Pydantic schemas with comprehensive validation
* Initial project setup
```

Vs. **Messy History** (before cleanup):
```
* Merge PR #3
* Updated files
* Fix typo
* Added stuff
* Merge develop
```

**Commit Message Format:**
```bash
# Good commits
git commit -m "Add Pydantic schemas for issue input and triage decision"
git commit -m "Add SQLAlchemy Triage model with tests"
git commit -m "Add FastAPI health check endpoint"

# Bad commits (avoid)
git commit -m "Update files"
git commit -m "Day 1 work"
```

**8. Documentation Preferences**
- NO emojis in README.md or any documentation (looks AI-generated)
- Use clean Markdown with proper headings
- Checkboxes for status: `- [x] Done` not "checkmark emoji Done"
- Professional, technical tone

---

**Status**: Day 1A Complete  
**Next Update**: After Day 1 full completion (schemas + models + FastAPI app)

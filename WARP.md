# WARP.md - AI Developer Toolkit

**Last Updated**: 2025-11-17 (22:18 UTC)  
**Current Status**: Day 1A - Complete (14 tests passing) - Schemas + Models + FastAPI  
**Branch**: `feature/schemas-setup`

---

## Quick Context

**Project**: AI-powered GitHub issue triage tool (learning project)  
**Goal**: Build FastAPI + LangGraph app that auto-classifies GitHub issues  
**Timeline**: 10 days (flexible), currently on Day 1

---

## Just Completed

**Day 1A: Schemas + Models + FastAPI Basics** ✅

**What Changed**:
1. Created `main.py`:
   - ✅ FastAPI app initialization
   - ✅ `GET /health` endpoint returning JSON
   - ✅ Uvicorn server setup (port 8081)
2. Created `tests/test_api.py`:
   - ✅ TestClient fixture
   - ✅ Health endpoint test
3. Added dependencies:
   - ✅ `httpx>=0.25.0` for TestClient support
4. Tests:
   - ✅ 14 total tests passing (8 schemas + 5 models + 1 API)

**Files Created**:
- `main.py` - FastAPI app with health endpoint
- `tests/test_api.py` - API endpoint tests

## Next Session: Day 1B Game Plan

**Goal**: Integrate OpenAI with async patterns, create business logic layer

**Estimated Time**: 1-2 hours

### Task 1: LLM Service (Async OpenAI Integration)
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

**Key Concepts**: `async`/`await`, OpenAI SDK, structured outputs, mocking async functions

---

### Task 2: Triage Service (Business Logic Layer)
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

**Key Concepts**: Mixing async (LLM) with sync (database), service layer pattern

---

### Dependencies to Add
```toml
[project]
dependencies = [
    # ... existing
    "openai>=1.0.0",        # OpenAI SDK
    "python-dotenv>=1.0.0", # Environment variables
]
```

### Environment Setup
```bash
# Create .env file
echo "OPENAI_API_KEY=your-key-here" > .env

# Add to .gitignore
echo ".env" >> .gitignore
```

### Acceptance Criteria
- [ ] LLM service returns valid `TriageDecision`
- [ ] Triage service saves to database
- [ ] All tests pass with mocked LLM responses
- [ ] ~20 tests passing total
- [ ] No real OpenAI API calls in tests (all mocked)

---

## Tech Stack

- **Backend**: FastAPI + SQLAlchemy (sync) + PostgreSQL
- **AI**: OpenAI GPT-4o-mini + LangGraph
- **Testing**: pytest + pytest-asyncio
- **Package Manager**: uv (faster than pip)
- **Python**: 3.12.9

---

## Key Decisions (Reference)

1. **TDD**: Strict Red-Green-Refactor (write tests first)
2. **Database**: Sync SQLAlchemy (not async) for pragmatism
3. **Learning Style**: Explain thoroughly first time, trust understanding after
4. **Code Style**: Type hints everywhere, docstrings on complex functions only
5. **No Emojis**: Professional docs (looks less AI-generated)
6. **Git Workflow**: Feature branches with PRs (main ← develop ← feature/*)

---

## Environment

**Location**: `/mnt/c/Repos/Personal/ai-dev-toolkit/services/api`  
**Venv**: `.venv` (activated via `uv-activate` bash function)  
**Current Branch**: `feature/schemas-setup`

**Quick Commands**:
```bash
# Activate venv
cd /mnt/c/Repos/Personal/ai-dev-toolkit/services/api
uv-activate

# Run tests
pytest -v

# Run specific test
pytest -k "test_name" -v
```

---

## Session Rules for Warp

1. **Always use TDD**: Write failing test → Implement → Pass test → Refactor
2. **Explain first encounter**: Full explanations with C#/TypeScript comparisons
3. **Trust after that**: Don't re-explain concepts user already understands
4. **Update both WARP.md and CLAUDE.md**: Keep them in sync
5. **No emojis**: Professional, technical tone
6. **Commit frequently**: After each passing test or complete feature

---

## Progress Tracker

### Day 1A Status
- [x] Setup uv venv
- [x] Create basic Pydantic schemas (`IssueInput`, `TriageDecision`)
- [x] Write 3 passing tests
- [x] Commit initial schemas to `feature/schemas-setup`
- [x] Enhance schemas with Literal types and Field validation
- [x] Expand test coverage to 8 tests (all passing)
- [x] Setup pytest-watcher for hot reload
- [x] Configure dev environment (WSL + Windows)
- [x] Commit and push enhanced schemas
- [x] Add SQLAlchemy models (Triage with 5 tests)
- [x] Create conftest.py with db_session fixture
- [x] Commit and push models
- [x] Add FastAPI basics (health check)
- [x] Add httpx dev dependency for TestClient
- [x] Write API endpoint tests (1 test passing)
- [x] Complete Day 1A (14 tests total)

---

## Next Steps

1. **Next Session**: Day 1B - LLM service integration (async OpenAI)
2. **Then**: Triage service (business logic layer)
3. **After That**: POST /api/triage endpoint

---

## Reference Links

- GitHub Repo: `https://github.com/lucachitayat/ai-dev-toolkit`
- Full Project Plan: See `CLAUDE.md`
- Current Working Dir: `/mnt/c/Repos/Personal/ai-dev-toolkit/services/api`

---

**For full context and architectural decisions, see `CLAUDE.md`**

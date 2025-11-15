# WARP.md - AI Developer Toolkit

**Last Updated**: 2025-11-15 (02:54 UTC)  
**Current Status**: Day 1A - Enhanced Schemas Complete (8 tests passing) -> Next: SQLAlchemy Models  
**Branch**: `feature/schemas-setup`

---

## Quick Context

**Project**: AI-powered GitHub issue triage tool (learning project)  
**Goal**: Build FastAPI + LangGraph app that auto-classifies GitHub issues  
**Timeline**: 10 days (flexible), currently on Day 1

---

## Just Completed

**Enhanced Pydantic Schemas with Validation** ✅

**What Changed**:
1. `IssueInput` schema:
   - ✅ Renamed `description` → `body` (matches GitHub API)
   - ✅ Added optional fields: `labels`, `author`, `created_at`
   - ✅ Used modern syntax: `str | None` instead of `Optional[str]`
2. `TriageDecision` schema:
   - ✅ Added `Literal` types for severity, category, priority (enum validation)
   - ✅ Added `confidence: float` with `Field(ge=0.0, le=1.0)`
3. Tests:
   - ✅ Expanded from 3 to 8 tests (all passing in 0.18s)
   - ✅ Added pytest-watcher for hot reload

**Files Modified**:
- `schemas.py` - Enhanced with Literal types and Field constraints
- `tests/test_schemas.py` - 8 comprehensive tests
- `.pytest-watcher.yaml` - Watch config (ignores .venv)

## Next Session

**Working On**: SQLAlchemy models with TDD (database layer)

**Files to Create**:
- `services/api/models.py` - Triage database model
- `services/api/tests/test_models.py` - Model tests

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
- [ ] Commit enhanced schemas
- [ ] Add SQLAlchemy models
- [ ] Create basic FastAPI app

---

## Next Steps

1. **Immediate**: Commit enhanced schemas to git
2. **Next**: SQLAlchemy models with TDD (Triage table)
3. **Then**: Basic FastAPI app with health check endpoint
4. **Tomorrow**: LLM service integration (async OpenAI)

---

## Reference Links

- GitHub Repo: `https://github.com/lucachitayat/ai-dev-toolkit`
- Full Project Plan: See `CLAUDE.md`
- Current Working Dir: `/mnt/c/Repos/Personal/ai-dev-toolkit/services/api`

---

**For full context and architectural decisions, see `CLAUDE.md`**

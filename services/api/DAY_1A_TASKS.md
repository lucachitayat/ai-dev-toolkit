# Day 1A: Detailed Task List

**Goal**: Complete Schemas + Models + Basic FastAPI App

**Status**: 2/4 sections complete ✅

---

## ✅ 1. Setup (COMPLETE)
- ✅ Created uv venv
- ✅ Created pyproject.toml
- ✅ Installed pytest + pytest-asyncio
- ✅ Created custom `uv-activate` bash function

---

## ✅ 2. Pydantic Schemas (COMPLETE)
- ✅ Created `schemas.py`
- ✅ Implemented `IssueInput` with title + description
- ✅ Implemented `TriageDecision` with severity, category, priority, labels, reasoning
- ✅ Wrote 3 tests (all passing)
- ✅ Fixed import issue (schemas/ directory mistake)

---

## 🎯 3. SQLAlchemy Models (NEXT - Estimated 1.5 hours)

### 3.1 Install Dependencies (5 min)
```bash
uv pip install sqlalchemy
```

### 3.2 Write Failing Test for Triage Model (15 min)
**File**: `tests/test_models.py`

**Test 1**: Model should have correct fields
```python
def test_triage_model_has_required_fields():
    """Triage model should have all required columns."""
    triage = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        title="Test issue",
        severity="high",
        category="bug",
        priority="P1",
        labels=["backend", "security"],
        reasoning="Test reasoning"
    )
    
    assert triage.title == "Test issue"
    assert triage.severity == "high"
    assert triage.labels == ["backend", "security"]
```

**Test 2**: Model should auto-generate timestamps
```python
def test_triage_model_auto_generates_timestamps():
    """Triage should have created_at set automatically."""
    triage = Triage(title="Test")
    # Before saving, created_at might be None
    # After db.session.add + commit, should have timestamp
```

**Run**: `pytest tests/test_models.py -v` (expect RED ❌)

---

### 3.3 Implement Triage Model (20 min)
**File**: `models.py`

```python
"""SQLAlchemy database models."""
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Triage(Base):
    """Triage decision record."""
    __tablename__ = "triages"
    
    id = Column(Integer, primary_key=True)
    issue_url = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    category = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    labels = Column(JSON, nullable=False)
    reasoning = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            "id": self.id,
            "issue_url": self.issue_url,
            "title": self.title,
            "severity": self.severity,
            "category": self.category,
            "priority": self.priority,
            "labels": self.labels,
            "reasoning": self.reasoning,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
```

**Key Points**:
- `Base = declarative_base()` - SQLAlchemy base class
- `__tablename__` - Database table name
- `Column` types map to SQL types
- `JSON` column for lists (stores as JSONB in PostgreSQL)
- `to_dict()` for serialization (like you had in IHX)

---

### 3.4 Setup Test Database (20 min)
**File**: `tests/conftest.py` (pytest configuration)

```python
"""Pytest configuration and fixtures."""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


@pytest.fixture(scope="function")
def db_session():
    """Create in-memory SQLite database for testing."""
    # Use SQLite in-memory for fast tests
    engine = create_engine("sqlite:///:memory:")
    
    # Create all tables
    Base.metadata.create_all(engine)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    # Cleanup after test
    session.close()
```

**Key Points**:
- `sqlite:///:memory:` - Temporary database (fast, isolated)
- `scope="function"` - New database for each test (no test pollution)
- `yield` - Provides session to test, then cleans up

---

### 3.5 Update Tests to Use Database (15 min)
**File**: `tests/test_models.py`

```python
"""Tests for SQLAlchemy models."""
from models import Triage


def test_triage_model_saves_to_database(db_session):
    """Triage should save and retrieve from database."""
    triage = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        title="Test issue",
        severity="high",
        category="bug",
        priority="P1",
        labels=["backend"],
        reasoning="Test"
    )
    
    db_session.add(triage)
    db_session.commit()
    
    # Retrieve from database
    saved = db_session.query(Triage).first()
    assert saved.title == "Test issue"
    assert saved.severity == "high"
    assert saved.id is not None  # Auto-generated


def test_triage_to_dict_serializes_correctly(db_session):
    """Triage.to_dict() should return valid dictionary."""
    triage = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        title="Test",
        severity="low",
        category="docs",
        priority="P3",
        labels=[],
        reasoning="Minor"
    )
    
    db_session.add(triage)
    db_session.commit()
    
    result = triage.to_dict()
    assert result["title"] == "Test"
    assert result["severity"] == "low"
    assert "created_at" in result
```

**Run**: `pytest tests/test_models.py -v` (expect GREEN ✅)

---

### 3.6 Acceptance Criteria for Section 3
- ✅ SQLAlchemy installed
- ✅ `models.py` created with Triage model
- ✅ `conftest.py` created with db_session fixture
- ✅ Tests passing (2+ tests green)
- ✅ Can save and retrieve Triage records

**Estimated Total**: 1.5 hours

---

## 4. Basic FastAPI App (Estimated 1 hour)

### 4.1 Install FastAPI + Uvicorn (5 min)
```bash
uv pip install fastapi uvicorn[standard]
```

**Why uvicorn[standard]?** Includes performance extras (websockets, etc.)

---

### 4.2 Write Failing Test for Health Endpoint (10 min)
**File**: `tests/test_app.py`

```python
"""Tests for FastAPI application."""
from fastapi.testclient import TestClient


def test_health_endpoint_returns_200():
    """GET /health should return 200 OK."""
    from main import app
    
    client = TestClient(app)
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

**Run**: `pytest tests/test_app.py -v` (expect RED ❌)

---

### 4.3 Implement Basic FastAPI App (20 min)
**File**: `main.py`

```python
"""FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Developer Toolkit API",
    description="AI-powered developer tools",
    version="0.1.0"
)

# Enable CORS (for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
```

**Key Points**:
- `FastAPI()` - Creates app instance
- `@app.get()` - Decorator for GET endpoint (like Flask's `@app.route()`)
- CORS middleware - Allows React frontend to call API
- `uvicorn.run()` - Development server (like `flask run`)

**Run**: `pytest tests/test_app.py -v` (expect GREEN ✅)

---

### 4.4 Test Running Locally (10 min)

**Start the server**:
```bash
python main.py
```

**In another terminal**:
```bash
curl http://localhost:8081/health
# Expected: {"status":"ok"}
```

**Or visit in browser**: http://localhost:8081/docs (automatic Swagger docs!)

---

### 4.5 Acceptance Criteria for Section 4
- ✅ FastAPI + uvicorn installed
- ✅ `main.py` created with basic app
- ✅ `/health` endpoint working
- ✅ Tests passing
- ✅ Can run locally: `python main.py`
- ✅ Swagger docs visible at `/docs`

**Estimated Total**: 1 hour

---

## Day 1A Summary

**Total Time Estimate**: ~4 hours (2 hours complete, 2.5 hours remaining)

**What We'll Have**:
- ✅ Pydantic schemas for validation
- ✅ SQLAlchemy model for database
- ✅ Basic FastAPI app with health check
- ✅ All tests passing (TDD discipline maintained)
- ✅ Ready to add LLM service next (Day 1B)

**Dependencies Added** (will update pyproject.toml at end):
- pydantic
- sqlalchemy
- fastapi
- uvicorn[standard]
- pytest
- pytest-asyncio

---

## When You Return from Break

**Start here:**
1. Navigate to `services/api/`
2. Activate venv: `uv-activate`
3. Go to **Section 3.1**: Install SQLAlchemy
4. Follow tasks in order
5. Celebrate each ✅!

**Questions?** Check CLAUDE.md or ask when you resume.

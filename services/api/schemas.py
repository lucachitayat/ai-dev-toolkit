from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


class IssueInput(BaseModel):
    """GitHub Issue input for triage"""

    title: str
    body: str
    labels: list[str] = []
    author: str | None = None
    created_at: datetime | None = None


class TriageDecision(BaseModel):
    """Triage decision output"""

    severity: Literal["critical", "high", "medium", "low"]
    category: Literal["bug", "feature", "docs", "refactor", "chore"]
    priority: Literal["P0", "P1", "P2", "P3", "P4"]
    labels: list[str]
    reasoning: str
    confidence: float = Field(ge=0.0, le=1.0)  # type: ignore

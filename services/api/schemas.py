from pydantic import BaseModel

class IssueInput(BaseModel):
    """GiHub Issue input for triage"""
    title: str
    description: str

class TriageDecision(BaseModel):
    """Triage decision output"""
    severity: str
    category: str
    priority: str
    labels: list[str]
    reasoning: str
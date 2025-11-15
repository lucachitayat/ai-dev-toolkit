import pytest
from pydantic import ValidationError
from schemas import IssueInput, TriageDecision
from datetime import datetime


def test_issue_input_validates_required_fields():
    """Issue input should accept a title and body"""

    current_time = datetime.now()

    issue = IssueInput(
        title="Test Title",
        body="Test Body",
        labels=["test", "test2"],
        author="test@test.com",
        created_at=current_time,
    )

    assert issue.title == "Test Title"
    assert issue.body == "Test Body"
    assert issue.labels == ["test", "test2"]
    assert issue.author == "test@test.com"
    assert issue.created_at == current_time


def test_issue_input_validates_optional_fields():
    """Issue input should accept a title and body"""
    issue = IssueInput(title="Test Title", body="Test Body")

    assert issue.title == "Test Title"
    assert issue.body == "Test Body"
    assert issue.labels == []
    assert issue.author is None
    assert issue.created_at is None


def test_issue_input_rejects_missing_title():
    """Issue input should reject a missing title"""
    with pytest.raises(ValidationError) as exc_info:
        IssueInput(body="Test Body")
    assert "title" in str(exc_info.value).lower()



def test_issue_input_rejects_missing_body():
    """Issue input should reject a missing body"""
    with pytest.raises(ValidationError) as exc_info:
        IssueInput(title="Test Title")
    assert "body" in str(exc_info.value).lower()


def test_triage_decision_rejects_invalid_severity():
    """Triage decision should reject an invalid severity"""
    with pytest.raises(ValidationError) as exc_info:
        TriageDecision(
            severity="super-critical",
            category="bug",
            priority="P1",
            labels=["bug"],
            reasoning="Test reasoning",
            confidence=0.95,
        )
    assert "severity" in str(exc_info.value).lower()


def test_triage_decision_rejects_invalid_category():
    """Triage decision should reject an invalid category"""
    with pytest.raises(ValidationError) as exc_info:
        TriageDecision(
            severity="critical",
            category="invalid",
            priority="P1",
            labels=["bug"],
            reasoning="Test reasoning",
            confidence=0.95,
        )
    assert "category" in str(exc_info.value).lower()


def test_triage_decision_rejects_invalid_priority():
    """Triage decision should reject an invalid priority"""
    with pytest.raises(ValidationError) as exc_info:
        TriageDecision(
            severity="critical",
            category="bug",
            priority="invalid",
            labels=["bug"],
            reasoning="Test reasoning",
            confidence=0.95,
        )
    assert "priority" in str(exc_info.value).lower()


def test_triage_decision_rejects_invalid_confidence():
    """Triage decision should reject an invalid confidence"""
    with pytest.raises(ValidationError) as exc_info:
        TriageDecision(
            severity="critical",
            category="bug",
            priority="P1",
            labels=["bug"],
            reasoning="Test reasoning",
            confidence=1.01,
        )
    assert "confidence" in str(exc_info.value).lower()

import pytest
from pydantic import ValidationError
from schemas import IssueInput, TriageDecision

def test_issue_input_validates_required_fields():
    """Issue input should accept a title and description"""
    issue = IssueInput(title="Test Title", description="Test Description")

    assert issue.title == "Test Title"
    assert issue.description == "Test Description"

def test_issue_input_validates_optional_fields():
    """Issue input should accept a title and description"""
    issue = IssueInput(title="Test Title", description="Test Description")

    assert issue.title == "Test Title"
    assert issue.description == "Test Description"

def test_issue_input_rejects_missing_title():
    """Issue input should reject a missing title"""
    with pytest.raises(ValidationError) as exc_info:
        IssueInput(description="Test Description")
    assert "title" in str(exc_info.value).lower()



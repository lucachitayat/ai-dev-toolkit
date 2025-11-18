import pytest
from schemas import IssueInput, TriageDecision
from core.llm_service import classify_issue


@pytest.mark.asyncio
async def test_classify_issue_success(mock_openai_client):
    issue = IssueInput(title="Test Title", body="Test Body")

    expected_result = TriageDecision(
        severity="low",
        category="feature",
        priority="P0",
        labels=["test", "test2"],
        reasoning="Test reasoning",
        confidence=0.95,
    )

    result = await classify_issue(issue, mock_openai_client)

    assert result == expected_result

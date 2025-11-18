import os
from schemas import IssueInput, TriageDecision
from openai import AsyncOpenAI, ChatCompletion
from core.prompts import TRIAGE_SYSTEM_PROMPT


async def classify_issue(
    issue: IssueInput, client: AsyncOpenAI = None
) -> TriageDecision:
    """Classify an issue into a triage decision"""

    if client is None:
        client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": TRIAGE_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Issue Title: {issue.title}\nIssue Body: {issue.body}",
            },
        ],
        response_format=TriageDecision,
    )

    return parse_response(response)


def parse_response(response: ChatCompletion) -> TriageDecision:
    """Parse the response from the LLM"""
    return TriageDecision.model_validate_json(response.choices[0].message.content)

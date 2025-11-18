from unittest.mock import AsyncMock

import pytest
from openai import OpenAI
from openai.types import CompletionUsage
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.chat.chat_completion import Choice
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base


@pytest.fixture
def db_session():
    """Create in-memory SQLite database for testing."""
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    yield session
    session.close()


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client for testing"""
    mock_client = AsyncMock(spec=OpenAI)

    fake_response = ChatCompletion(
        id="test-id",
        object="chat.completion",
        created=1234567890,
        model="gpt-4o-mini",
        choices=[
            Choice(
                index=0,
                message=ChatCompletionMessage(
                    role="assistant",
                    content='{"severity": "low", "category": "feature", "priority": "P0", "labels": ["test", "test2"], "reasoning": "Test reasoning", "confidence": 0.95}',
                ),
                finish_reason="stop",
            )
        ],
        usage=CompletionUsage(prompt_tokens=10, completion_tokens=20, total_tokens=30),
    )

    # Make create() awaitable
    mock_client.chat.completions.create = AsyncMock(return_value=fake_response)

    return mock_client

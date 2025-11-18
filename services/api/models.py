from datetime import datetime, timezone
from sqlalchemy import Column, Float, Integer, String, Text, JSON, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Triage(Base):
    """Triage decision record."""

    __tablename__ = "triages"

    id: int = Column(Integer, primary_key=True)
    issue_url: str = Column(String, unique=True, nullable=False)
    title: str = Column(String, nullable=False)
    body: str = Column(String, nullable=False)
    severity: str = Column(String, nullable=False)
    category: str = Column(String, nullable=False)
    priority: str = Column(String, nullable=False)
    labels: JSON = Column(JSON, nullable=False)
    reasoning: str = Column(Text, nullable=False)
    confidence: float = Column(Float, nullable=False)
    created_at: datetime = Column(DateTime, default=lambda: datetime.now(timezone.utc))

import pytest
from sqlalchemy.exc import IntegrityError
from models import Triage


def test_triage_model_has_required_fields(db_session):
    """Triage model should have all required fields"""

    triage = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        body="Test body",
        title="Test issue",
        severity="high",
        category="bug",
        priority="P1",
        labels=["bug"],
        reasoning="Test reasoning",
        confidence=0.95,
    )

    db_session.add(triage)
    db_session.commit()

    assert triage.issue_url == "https://github.com/user/repo/issues/1"
    assert triage.id > 0
    assert triage.title == "Test issue"
    assert triage.created_at is not None


def test_triage_unique_issue_url(db_session):
    """Triage model should have a unique issue URL"""
    triage1 = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        title="Test issue",
        body="Test body",
        severity="high",
        category="bug",
        priority="P1",
        labels=["bug"],
        reasoning="Test reasoning",
        confidence=0.95,
    )

    db_session.add(triage1)
    db_session.commit()

    triage2 = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        title="Test issue",
        body="Test body",
        severity="high",
        category="bug",
        priority="P1",
        labels=["bug"],
        reasoning="Test reasoning",
        confidence=0.95,
    )

    db_session.add(triage2)
    with pytest.raises(IntegrityError):
        db_session.commit()

    db_session.rollback()


def test_triage_model_assigns_all_fields(db_session):
    """Triage model should assign all fields"""
    triage = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        title="Test issue",
        body="Test body",
        severity="high",
        category="bug",
        priority="P1",
        labels=["bug"],
        reasoning="Test reasoning",
        confidence=0.95,
    )
    db_session.add(triage)
    db_session.commit()

    saved = db_session.query(Triage).first()
    assert saved.issue_url == "https://github.com/user/repo/issues/1"
    assert saved.title == "Test issue"
    assert saved.body == "Test body"
    assert saved.severity == "high"
    assert saved.category == "bug"
    assert saved.priority == "P1"
    assert saved.labels == ["bug"]
    assert saved.reasoning == "Test reasoning"
    assert saved.confidence == 0.95
    assert saved.created_at is not None


def test_triage_has_unique_id(db_session):
    """Triage model should have a unique ID"""
    triage1 = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        title="Test issue",
        body="Test body",
        severity="high",
        category="bug",
        priority="P1",
        labels=["bug"],
        reasoning="Test reasoning",
        confidence=0.95,
    )
    db_session.add(triage1)
    db_session.commit()

    triage2 = Triage(
        issue_url="https://github.com/user/repo/issues/2",
        title="Test issue",
        body="Test body",
        severity="high",
        category="bug",
        priority="P1",
        labels=["bug"],
        reasoning="Test reasoning",
        confidence=0.95,
    )
    db_session.add(triage2)
    db_session.commit()

    assert triage1.id != triage2.id


def test_triage_cannot_set_used_id(db_session):
    """Triage model should not allow setting the ID if it is already used"""
    triage1 = Triage(
        issue_url="https://github.com/user/repo/issues/1",
        title="Test issue",
        body="Test body",
        severity="high",
        category="bug",
        priority="P1",
        labels=["bug"],
        reasoning="Test reasoning",
        confidence=0.95,
    )
    db_session.add(triage1)
    db_session.commit()

    triage2 = Triage(
        id=triage1.id,
        issue_url="https://github.com/user/repo/issues/2",
        title="Test issue",
        body="Test body",
        severity="high",
        category="bug",
        priority="P1",
        labels=["bug"],
        reasoning="Test reasoning",
        confidence=0.95,
    )
    db_session.add(triage2)
    with pytest.raises(IntegrityError):
        db_session.commit()

    db_session.rollback()

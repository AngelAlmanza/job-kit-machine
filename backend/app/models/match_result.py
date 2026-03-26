from datetime import datetime
from typing import Any, Optional

from sqlalchemy import Column, DateTime, Index, JSON, SmallInteger, String, UniqueConstraint, func, text
from sqlmodel import Field, SQLModel


class MatchResult(SQLModel, table=True):
    __tablename__ = "match_result"
    __table_args__ = (
        Index("ix_match_score_overall", "score_overall"),
        Index("ix_match_classification", "classification"),
        UniqueConstraint("job_id", name="uq_match_result_job_id"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int = Field(foreign_key="job.id", nullable=False)
    score_overall: int = Field(sa_column=Column(SmallInteger(), nullable=False))
    score_skills: int = Field(sa_column=Column(SmallInteger(), nullable=False))
    score_experience: int = Field(sa_column=Column(SmallInteger(), nullable=False))
    score_education: int = Field(sa_column=Column(SmallInteger(), nullable=False))
    score_languages: int = Field(sa_column=Column(SmallInteger(), nullable=False))
    score_preferences: int = Field(sa_column=Column(SmallInteger(), nullable=False))
    classification: str = Field(sa_column=Column(String(20), nullable=False))
    summary: str = Field(sa_column=Column(String, nullable=False))
    matching_skills: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    gap_skills: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    differentiators: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    raw_response: Optional[Any] = Field(
        default=None, sa_column=Column(JSON, nullable=True)
    )
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

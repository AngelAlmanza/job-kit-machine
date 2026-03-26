from datetime import date, datetime
from typing import Any, Optional

from sqlalchemy import Column, DateTime, JSON, String, func, text
from sqlmodel import Field, SQLModel


class WorkExperience(SQLModel, table=True):
    __tablename__ = "work_experience"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", nullable=False)
    company: str = Field(sa_column=Column(String(200), nullable=False))
    job_title: str = Field(sa_column=Column(String(200), nullable=False))
    start_date: date = Field(nullable=False)
    end_date: Optional[date] = Field(default=None)
    is_current: bool = Field(default=False)
    description: str = Field(sa_column=Column(String, nullable=False))
    technologies: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    sort_order: int = Field(default=0)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        ),
    )

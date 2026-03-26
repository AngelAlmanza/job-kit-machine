from datetime import datetime
from typing import Any, Optional

from sqlalchemy import Column, DateTime, JSON, String, func, text
from sqlmodel import Field, SQLModel


class Search(SQLModel, table=True):
    __tablename__ = "search"

    id: Optional[int] = Field(default=None, primary_key=True)
    job_title: str = Field(sa_column=Column(String(200), nullable=False))
    location: Optional[str] = Field(default=None, sa_column=Column(String(200)))
    modality: Optional[str] = Field(default=None, sa_column=Column(String(20)))
    keywords: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    platforms: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    is_scheduled: bool = Field(default=False)
    schedule_cron: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    schedule_active: bool = Field(default=False)
    last_run_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    next_run_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    status: str = Field(
        default="pending",
        sa_column=Column(String(20), nullable=False, server_default=text("'pending'")),
    )
    jobs_found: int = Field(default=0)
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

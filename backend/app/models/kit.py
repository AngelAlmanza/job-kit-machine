from datetime import datetime
from typing import Any, Optional

from sqlalchemy import Column, DateTime, Index, JSON, SmallInteger, String, func, text
from sqlmodel import Field, SQLModel


class Kit(SQLModel, table=True):
    __tablename__ = "kit"
    __table_args__ = (Index("ix_kit_job_version", "job_id", "version"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int = Field(foreign_key="job.id", nullable=False)
    version: int = Field(
        default=1,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("1")),
    )
    cv_html: str = Field(sa_column=Column(String, nullable=False))
    cv_pdf_path: Optional[str] = Field(default=None, sa_column=Column(String(500)))
    email_subject: Optional[str] = Field(default=None, sa_column=Column(String(300)))
    email_body: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))
    short_message: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))
    strengths: Optional[Any] = Field(default=None, sa_column=Column(JSON, nullable=True))
    weaknesses: Optional[Any] = Field(default=None, sa_column=Column(JSON, nullable=True))
    study_guide: Optional[Any] = Field(default=None, sa_column=Column(JSON, nullable=True))
    raw_response: Optional[Any] = Field(default=None, sa_column=Column(JSON, nullable=True))
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

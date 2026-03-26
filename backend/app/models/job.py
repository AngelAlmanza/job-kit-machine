from datetime import date, datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Index, String, UniqueConstraint, func, text
from sqlmodel import Field, SQLModel


class Job(SQLModel, table=True):
    __tablename__ = "job"
    __table_args__ = (
        Index("ix_job_status", "status"),
        Index("ix_job_platform", "platform"),
        UniqueConstraint("source_url", name="ux_job_source_url"),
        UniqueConstraint("company", "title", name="ux_job_company_title"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(sa_column=Column(String(300), nullable=False))
    company: str = Field(sa_column=Column(String(200), nullable=False))
    location: str = Field(sa_column=Column(String(200), nullable=False))
    modality: Optional[str] = Field(default=None, sa_column=Column(String(20)))
    description: str = Field(sa_column=Column(String, nullable=False))
    requirements: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))
    salary_min: Optional[int] = Field(default=None)
    salary_max: Optional[int] = Field(default=None)
    salary_currency: Optional[str] = Field(default=None, sa_column=Column(String(10)))
    published_at: date = Field(nullable=False)
    platform: str = Field(sa_column=Column(String(20), nullable=False))
    source_url: str = Field(sa_column=Column(String(1000), nullable=False))
    status: str = Field(
        default="nueva",
        sa_column=Column(String(20), nullable=False, server_default=text("'nueva'")),
    )
    found_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )
    seen_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime(timezone=True), nullable=True)
    )
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

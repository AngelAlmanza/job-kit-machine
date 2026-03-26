from datetime import datetime
from typing import Any, Optional

from sqlalchemy import Column, DateTime, JSON, String, UniqueConstraint, func, text
from sqlmodel import Field, SQLModel


class JobPreference(SQLModel, table=True):
    __tablename__ = "job_preference"
    __table_args__ = (UniqueConstraint("profile_id", name="uq_job_preference_profile_id"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", nullable=False)
    salary_min: Optional[int] = Field(default=None)
    salary_max: Optional[int] = Field(default=None)
    salary_currency: Optional[str] = Field(
        default="MXN",
        sa_column=Column(String(10), nullable=False, server_default=text("'MXN'")),
    )
    modalities: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    preferred_locations: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    contract_types: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
    )
    willing_to_relocate: bool = Field(default=False)
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

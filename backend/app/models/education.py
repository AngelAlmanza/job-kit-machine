from datetime import date, datetime
from typing import Optional

from sqlalchemy import Column, DateTime, String, func
from sqlmodel import Field, SQLModel


class Education(SQLModel, table=True):
    __tablename__ = "education"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", nullable=False)
    institution: str = Field(sa_column=Column(String(200), nullable=False))
    degree: str = Field(sa_column=Column(String(200), nullable=False))
    start_date: Optional[date] = Field(default=None)
    end_date: Optional[date] = Field(default=None)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

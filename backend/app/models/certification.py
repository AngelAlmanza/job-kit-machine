from datetime import date, datetime
from typing import Optional

from sqlalchemy import Column, DateTime, String, func
from sqlmodel import Field, SQLModel


class Certification(SQLModel, table=True):
    __tablename__ = "certification"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", nullable=False)
    name: str = Field(sa_column=Column(String(200), nullable=False))
    issuer: str = Field(sa_column=Column(String(200), nullable=False))
    obtained_date: Optional[date] = Field(default=None)
    verification_url: Optional[str] = Field(default=None, sa_column=Column(String(500)))
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

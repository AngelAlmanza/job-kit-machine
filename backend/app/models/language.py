from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, String, func
from sqlmodel import Field, SQLModel


class Language(SQLModel, table=True):
    __tablename__ = "language"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", nullable=False)
    name: str = Field(sa_column=Column(String(100), nullable=False))
    level: str = Field(sa_column=Column(String(20), nullable=False))
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

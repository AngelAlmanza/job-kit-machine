from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, String, func
from sqlmodel import Field, SQLModel


class Course(SQLModel, table=True):
    __tablename__ = "course"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", nullable=False)
    name: str = Field(sa_column=Column(String(200), nullable=False))
    platform: str = Field(sa_column=Column(String(200), nullable=False))
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

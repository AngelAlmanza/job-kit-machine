from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, SmallInteger, String, func
from sqlmodel import Field, SQLModel


class Skill(SQLModel, table=True):
    __tablename__ = "skill"

    id: Optional[int] = Field(default=None, primary_key=True)
    profile_id: int = Field(foreign_key="profile.id", nullable=False)
    name: str = Field(sa_column=Column(String(100), nullable=False))
    level: str = Field(sa_column=Column(String(20), nullable=False))
    years_experience: Optional[int] = Field(
        default=None, sa_column=Column(SmallInteger(), nullable=True)
    )
    category: str = Field(sa_column=Column(String(50), nullable=False))
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, text
from sqlmodel import Field, SQLModel


class Notification(SQLModel, table=True):
    __tablename__ = "notification"

    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: Optional[int] = Field(
        default=None,
        sa_column=Column(Integer, ForeignKey("job.id", ondelete="SET NULL"), nullable=True),
    )
    search_id: Optional[int] = Field(default=None, foreign_key="search.id", nullable=True)
    type: str = Field(sa_column=Column(String(30), nullable=False))
    title: str = Field(sa_column=Column(String(200), nullable=False))
    message: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))
    is_read: bool = Field(default=False)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False),
    )

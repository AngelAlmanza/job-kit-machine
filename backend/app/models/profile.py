from datetime import datetime
from typing import Any, Optional

from sqlalchemy import Column, DateTime, JSON, String, func, text
from sqlmodel import Field, SQLModel


class Profile(SQLModel, table=True):
    __tablename__ = "profile"

    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str = Field(sa_column=Column(String(200), nullable=False))
    email: str = Field(sa_column=Column(String(200), nullable=False))
    phone: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    city: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    state: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    country: Optional[str] = Field(
        default="México",
        sa_column=Column(String(100), nullable=False, server_default=text("'México'")),
    )
    linkedin_url: Optional[str] = Field(default=None, sa_column=Column(String(500)))
    github_url: Optional[str] = Field(default=None, sa_column=Column(String(500)))
    portfolio_url: Optional[str] = Field(default=None, sa_column=Column(String(500)))
    other_links: Optional[Any] = Field(
        default=None,
        sa_column=Column(JSON, nullable=False, server_default=text("'[]'::json")),
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

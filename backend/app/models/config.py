from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, SmallInteger, String, func, text
from sqlmodel import Field, SQLModel


class Config(SQLModel, table=True):
    __tablename__ = "config"

    id: Optional[int] = Field(default=None, primary_key=True)
    llm_provider: str = Field(
        default="ollama",
        sa_column=Column(String(20), nullable=False, server_default=text("'ollama'")),
    )
    llm_model: str = Field(sa_column=Column(String(100), nullable=False))
    llm_api_key: Optional[str] = Field(default=None, sa_column=Column(String(500)))
    threshold_apply_now: int = Field(
        default=80,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("80")),
    )
    threshold_good_match: int = Field(
        default=60,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("60")),
    )
    threshold_study_first: int = Field(
        default=40,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("40")),
    )
    weight_skills: int = Field(
        default=35,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("35")),
    )
    weight_experience: int = Field(
        default=25,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("25")),
    )
    weight_education: int = Field(
        default=15,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("15")),
    )
    weight_languages: int = Field(
        default=10,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("10")),
    )
    weight_preferences: int = Field(
        default=15,
        sa_column=Column(SmallInteger(), nullable=False, server_default=text("15")),
    )
    cv_template_path: Optional[str] = Field(default=None, sa_column=Column(String(500)))
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

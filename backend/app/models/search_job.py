from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


class SearchJob(SQLModel, table=True):
    __tablename__ = "search_job"
    __table_args__ = (UniqueConstraint("search_id", "job_id", name="uq_search_job"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    search_id: int = Field(foreign_key="search.id", nullable=False)
    job_id: int = Field(foreign_key="job.id", nullable=False)

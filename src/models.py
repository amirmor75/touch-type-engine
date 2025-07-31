from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Drill(Base):
    __tablename__ = "drills"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True) 
    text: Mapped[str] = mapped_column(Text)
    type: Mapped[str] = mapped_column(String(100))
    tags: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    topic: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

class Session(Base):
    __tablename__ = 'sessions'
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(36))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    wpm: Mapped[float] = mapped_column(Float)
    accuracy: Mapped[float] = mapped_column(Float)
    drill_id: Mapped[str] = mapped_column(String(36))
    error_words: Mapped[str] = mapped_column(Text)
    slow_suffixes: Mapped[str] = mapped_column(Text)
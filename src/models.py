from datetime import datetime

from sqlalchemy import Column, DateTime, Float, String, Text

from src.db import Base

class Paragraph(Base):
    __tablename__ = 'paragraphs'
    id = Column(String, primary_key=True)
    text = Column(Text)
    topic = Column(String)

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(String, primary_key=True)
    user_id = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    wpm = Column(Float)
    accuracy = Column(Float)
    paragraph_id = Column(String)
    error_words = Column(Text)         # comma-separated for SQLite
    slow_suffixes = Column(Text)       # comma-separated for SQLite

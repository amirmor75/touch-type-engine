from fastapi import APIRouter
from src.models import Session
from src.db import SessionLocal
from src.schemas import SessionData
import uuid

router = APIRouter()

@router.post("/")
def submit_session(data: SessionData):
    db = SessionLocal()
    session = Session(
        id=str(uuid.uuid4()),
        user_id=data.user_id,
        wpm=data.wpm,
        accuracy=data.accuracy,
        paragraph_id=data.paragraph_id,
        error_words=",".join(data.error_words),
        slow_suffixes=",".join(data.slow_suffixes)
    )
    db.add(session)
    db.commit()
    return {"status": "saved", "id": session.id}

from fastapi import APIRouter
from src.db import SessionLocal
from src.models import Paragraph
import random

router = APIRouter()

@router.get("/")
def get_paragraph():
    db = SessionLocal()
    paras = db.query(Paragraph).all()
    if not paras:
        return {"text": "No paragraphs available"}
    para = random.choice(paras)
    return {
        "id": para.id,
        "text": para.text,
        "topic": para.topic
    }

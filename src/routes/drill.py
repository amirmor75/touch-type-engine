from fastapi import APIRouter, Header, HTTPException
from sqlalchemy.orm import Session
from src.db import SessionLocal
from src.models import Drill

import random

router = APIRouter()

@router.get("/")
def get_drill(drill_number: int = Header(None)):
    db: Session = SessionLocal()

    if drill_number is not None:
        drill = db.query(Drill).filter(Drill.id == drill_number).first()
        if not drill:
            raise HTTPException(status_code=404, detail="Drill not found")
    else:
        drills = db.query(Drill).all()
        if not drills:
            return {"text": "No drills available"}
        drill = random.choice(drills)

    return {
        "id": drill.id,
        "text": drill.text,
        "topic": drill.topic
    }



from pydantic import BaseModel
from typing import List

class SessionData(BaseModel):
    user_id: str
    wpm: float
    accuracy: float
    paragraph_id: str
    error_words: List[str]
    slow_suffixes: List[str]

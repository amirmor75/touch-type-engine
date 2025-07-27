from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.db import init_db
from src.routes import paragraph, session

load_dotenv()  # Load .env file
app = FastAPI()

# Enable CORS (allow frontend at Vite default port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Initialize DB schema
init_db()

@app.get("/ping")
def ping():
    return {"message": "pong"}

# Register routes
app.include_router(paragraph.router, prefix="/paragraph")
app.include_router(session.router, prefix="/session")

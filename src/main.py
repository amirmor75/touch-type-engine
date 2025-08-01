from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.routes import drill,session
from src.db import init_db

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("starting lifespan", flush=True)
    init_db()
    yield
    # Cleanup can be added here if needed


app = FastAPI(lifespan=lifespan)


# Enable CORS (allow frontend at Vite default port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/ping")
def ping():
    return {"message": "pong"}

# Register routes
app.include_router(drill.router, prefix="/drill")
app.include_router(session.router, prefix="/session")

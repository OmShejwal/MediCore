import os
import sys
# Add current directory to sys.path to allow imports from local files
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, token, workout, meals, coach, progress
from database import init_db, SessionLocal, User
from services.auth import get_password_hash
import json

# Keep the app bootable even if heavy ML dependencies fail at import time.
try:
    from routers import predictions
except Exception as exc:
    predictions = None
    print(f"Warning: predictions router disabled due to import error: {exc}")
app = FastAPI(title="VaidyaAI - AI Health Platform", version="1.0.0")

# Initialize database immediately
init_db()

# CORS - Allow frontend from any origin for deployment flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5175",
        "https://*.netlify.app",  # Allow all Netlify subdomains
        "*"  # Allow all origins for demo/submission (remove in production)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    """Create default admin user if not exists"""
    # Create default admin user if not exists
    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.username == "admin").first()
        if not admin:
            admin_user = User(
                username="admin",
                email="admin@sehatsaathi.com",
                full_name="Admin User",
                hashed_password=get_password_hash("admin123"),
                fitness_level="intermediate",
                fitness_goal="maintenance"
            )
            db.add(admin_user)
            db.commit()
            print("Admin user created successfully")
    finally:
        db.close()


app.include_router(users.router)
app.include_router(token.router)
app.include_router(workout.router)
app.include_router(meals.router)
app.include_router(coach.router)
app.include_router(progress.router)
if predictions is not None:
    app.include_router(predictions.router)

# Print all registered routes for debugging
for route in app.routes:
    print(f"Route: {route.path} - Methods: {route.methods}")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "VaidyaAI Backend is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

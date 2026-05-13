# MediCore Backend

This folder contains the FastAPI backend for MediCore. It exposes authentication, coaching, diagnosis, scheme search, progress tracking, and mental health endpoints used by the frontend.

## Core Responsibilities

- User registration, login, and profile management.
- AROMI coach chat, meal plans, workout plans, and combined plans.
- Disease prediction APIs for clinical and image-based workflows.
- SahayakAI disability-scheme search and eligibility guidance.
- ManasMitra check-in, mood capture, and stress summaries.

## Backend Structure

- `main.py` - application entry point and router registration.
- `routers/` - feature-specific FastAPI routes.
- `services/` - Groq integration, auth helpers, scheme search logic.
- `database.py` - ORM models, session management, and database initialization.
- `schemas.py` - Pydantic request and response schemas.

## Local Setup

### Prerequisites

- Python 3.8+
- A Groq API key for live AI content

### Steps

1. Go to [Hackathon/backend](.).
2. Copy `.env.example` to `.env`.
3. Set `GROQ_API_KEY`, `SECRET_KEY`, and any deployment-specific values.
4. Install dependencies.

```bash
pip install -r requirements.txt
```

5. Start the backend.

```bash
python main.py
```

6. The server listens on `http://127.0.0.1:8002` by default.

## Environment Variables

- `GROQ_API_KEY` - AI model access key.
- `SECRET_KEY` - JWT signing secret.
- `DATABASE_URL` - database connection string.
- `CORS_ORIGINS` - allowed frontend origins.
- `ACCESS_TOKEN_EXPIRE_MINUTES` - token lifetime.

## Useful Endpoints

- `GET /health` - backend health check.
- `POST /register` - create a user.
- `POST /token` - log in and receive a JWT.
- `POST /coach/chat` - AROMI coach requests.
- `POST /sahayak/search` - disability scheme search.
- `POST /predictions/predict` - image diagnosis.
- `GET /manasmitra/summary` - mental health summary.

## Training Utilities

- [../src/train_ham10000.py](../src/train_ham10000.py) - skin lesion training script.
- [../src/train_lungs.py](../src/train_lungs.py) - lungs classifier training script.
- [../models/train_models.py](../models/train_models.py) - tabular model training utility.

## Notes

- The backend defaults to SQLite for local development.
- For production, use a managed database instead of the local SQLite file.
- If you change the backend port, update the frontend proxy in [frontend/vite.config.ts](../../frontend/vite.config.ts).

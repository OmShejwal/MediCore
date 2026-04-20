# VaidyaAI

VaidyaAI is an AI health platform that combines scan-based diagnosis, risk prediction, wellness coaching, disability scheme guidance, and mental health tracking in one workspace. The app is split into a React frontend and a FastAPI backend and is designed to run locally, in containers, or on cloud hosting platforms.

## What It Does

- Health dashboard with vitals, progress, achievements, and activity logging.
- AROMI AI Coach for meal plans, workout plans, and combined plans.
- Multi-organ prediction flows for skin, eye, oral, bone, lungs, diabetes, hypertension, and anemia.
- SahayakAI for disability scheme discovery, eligibility checks, and application guidance.
- ManasMitra for mental well-being check-ins, stress indexing, and reflection support.
- Hospital finder and profile/settings management.

## Repository Layout

- [frontend](frontend) - Vite + React application.
- [Hackathon/backend](Hackathon/backend) - FastAPI API and database layer.
- [Hackathon/src](Hackathon/src) - Model training and preprocessing utilities.
- [Hackathon/models](Hackathon/models) - Trained model artifacts.
- [deploy/aws](deploy/aws) - AWS deployment notes and container guidance.

## Tech Stack

- Frontend: React, Vite, TypeScript, Tailwind CSS, Shadcn UI, Framer Motion, React Query.
- Backend: FastAPI, SQLAlchemy, Pydantic, SQLite for local development.
- AI and ML: Groq, PyTorch, OpenCV, scikit-learn, DuckDuckGo search integration.

## Local Setup

### Prerequisites

- Python 3.8 or newer.
- Node.js 18 or newer.
- A Groq API key for live AI responses.

### Backend

1. Go to [Hackathon/backend](Hackathon/backend).
2. Copy `.env.example` to `.env` and set `GROQ_API_KEY` and `SECRET_KEY`.
3. Install dependencies with `pip install -r requirements.txt`.
4. Start the API with `python main.py`.
5. The backend listens on `http://127.0.0.1:8002` by default.

### Frontend

1. Go to [frontend](frontend).
2. Install dependencies with `npm install`.
3. Start the dev server with `npm run dev`.
4. The frontend runs on `http://localhost:8080`.

## Important Local Notes

- Frontend API calls are proxied to the backend on port `8002`.
- If the backend is not reachable, login-dependent pages will show authorization or connection errors.
- The backend can still return demo-mode content when the Groq key is not set, but live AI responses require the key.

## Useful Pages

- `/` - landing and dashboard entry.
- `/coach` - AROMI health coach.
- `/sahayak` - disability scheme navigator.
- `/manasmitra` - mental wellness tracking.
- `/diagnosis` - image-based diagnosis tools.

## Deployment

- Frontend hosting options are documented in [deploy/aws](deploy/aws).
- The backend can be containerized with the provided Docker files.
- For production, prefer PostgreSQL or another managed database instead of SQLite.

## Notes

- Do not commit real secret values to git.
- Large model artifacts are stored under [Hackathon/models](Hackathon/models).
- If you change the backend port, update the frontend proxy in [frontend/vite.config.ts](frontend/vite.config.ts).

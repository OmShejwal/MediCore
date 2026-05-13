# MediCore

MediCore is an AI health platform that combines scan-based diagnosis, risk prediction, wellness coaching, disability scheme guidance, and mental health tracking in one workspace. The app is split into a React frontend and a FastAPI backend and is designed to run locally, in containers, or on cloud hosting platforms.

## What It Does

- Health dashboard with vitals, progress, achievements, and activity logging.
- AROMI AI Coach for meal plans, workout plans, and combined plans.
- Multi-organ prediction flows for skin, eye, oral, bone, lungs, diabetes, hypertension, and anemia.
- SahayakAI for disability scheme discovery, eligibility checks, and application guidance.
- ManasMitra for mental well-being check-ins, stress indexing, and reflection support.
- Hospital finder and profile/settings management.

## Repository Layout

- [frontend](frontend) - Vite + React application.
- [backend](backend) - Deployable FastAPI entrypoint used by Render.
- [Hackathon/backend](Hackathon/backend) - Existing FastAPI implementation reused by the deploy entrypoint.
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

1. Go to [backend](backend).
2. Copy `.env.example` to `.env` and set `GROQ_API_KEY`, `SECRET_KEY`, and your production `DATABASE_URL` if needed.
3. Install dependencies with `pip install -r requirements.txt`.
4. Start the API with `python main.py` or `uvicorn main:app --reload --host 0.0.0.0 --port 8002`.
5. The backend listens on `http://127.0.0.1:8002` by default.

### Frontend

1. Go to [frontend](frontend).
2. Install dependencies with `npm install`.
3. Optionally create `frontend/.env.local` with `VITE_API_URL=https://your-backend-url.onrender.com` for direct Render API calls in production.
4. Start the dev server with `npm run dev`.
5. The frontend runs on `http://localhost:8080`.

## Important Local Notes

- Frontend API calls use `VITE_API_URL` when set, otherwise they fall back to `/api` in development.
- Netlify can rewrite `/api/*` to the Render backend, or you can point `VITE_API_URL` directly at the Render service.
- If the backend is not reachable, login-dependent pages will show authorization or connection errors.
- The backend can still return demo-mode content when the Groq key is not set, but live AI responses require the key.

## Useful Pages

- `/` - landing and dashboard entry.
- `/coach` - AROMI health coach.
- `/sahayak` - disability scheme navigator.
- `/manasmitra` - mental wellness tracking.
- `/diagnosis` - image-based diagnosis tools.

## Deployment

- Backend deployment: use [backend](backend) as the Render root, install from `requirements.txt`, and start with `uvicorn main:app --host 0.0.0.0 --port $PORT`.
- Frontend deployment: build [frontend](frontend) on Netlify with `npm run build` and set `VITE_API_URL` or keep the `/api` rewrite in `netlify.toml`.
- For production, prefer PostgreSQL or another managed database instead of SQLite.

## Notes

- Do not commit real secret values to git.
- Large model artifacts are stored under [Hackathon/models](Hackathon/models).
- If you change the backend port, update the frontend proxy in [frontend/vite.config.ts](frontend/vite.config.ts).

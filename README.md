# MediCore

A comprehensive AI-powered health and wellness platform designed to provide personalized coaching, disease prediction, accessibility support, and mental health services. MediCore combines modern web technologies with advanced machine learning to deliver a complete healthcare companion experience.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Running the Project](#running-the-project)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

MediCore is a full-stack healthcare platform that leverages AI and machine learning to assist users in their health journey. It provides:
- **AI-Powered Coaching** (AROMI Coach) for personalized fitness and nutrition guidance
- **Disease Prediction** through clinical data analysis and image-based diagnosis
- **Accessibility Support** (SahayakAI) for disability scheme discovery and eligibility guidance
- **Mental Health** (ManasMitra) check-ins with mood tracking and stress management
- **Activity & Progress Tracking** with comprehensive health metrics

## ✨ Features

### 1. **User Authentication & Management**
   - Secure registration and login
   - JWT-based authentication
   - Profile management
   - Password recovery functionality

### 2. **AI Coach (AROMI)**
   - Personalized fitness coaching via chat
   - Meal plan generation and customization
   - Workout plan creation and recommendations
   - Combined health plans based on user goals and medical conditions

### 3. **Health Prediction & Diagnosis**
   - Clinical-based disease prediction (Diabetes, Hypertension, Anemia)
   - Image-based diagnosis (Skin lesions, Lung conditions)
   - AI-powered health risk assessment
   - Model integration with deep learning (TensorFlow, PyTorch)

### 4. **SahayakAI - Accessibility & Disability Support**
   - Search disability schemes and welfare programs
   - Eligibility checking and guidance
   - Scheme recommendations based on user profile
   - Support for underserved populations

### 5. **ManasMitra - Mental Health**
   - Mental health check-ins
   - Mood and stress tracking
   - Wellness summaries and insights
   - Confidential health records

### 6. **Activity & Progress Tracking**
   - Real-time heart rate monitoring
   - Activity logging with detailed metrics
   - Achievement tracking and badges
   - Progress visualization with charts

### 7. **Hospital Finder**
   - Locate nearby healthcare facilities
   - Hospital information and ratings
   - Emergency services directory

### 8. **Responsive Dashboard**
   - Comprehensive health overview
   - Quick action buttons
   - Vital cards with health metrics
   - Motivational quotes and encouragement

## 🛠 Tech Stack

### Frontend
- **Framework**: React 18+ with TypeScript
- **Build Tool**: Vite
- **UI Library**: shadcn/ui with Radix UI components
- **Styling**: Tailwind CSS
- **State Management**: React Query (TanStack Query)
- **Form Handling**: React Hook Form with Zod validation
- **Testing**: Vitest
- **Routing**: React Router v6
- **Icons**: Lucide React

### Backend
- **Framework**: FastAPI (Python)
- **Server**: Uvicorn
- **Database**: SQLAlchemy ORM with SQLite (local) / PostgreSQL (production)
- **Authentication**: JWT with python-jose
- **AI Integration**: Groq API for LLM services, LangChain for AI workflows
- **Image Processing**: OpenCV, Pillow, DeepFace
- **ML Models**: TensorFlow, PyTorch for predictions
- **Search**: DuckDuckGo integration
- **Email Validation**: Pydantic with email-validator

### DevOps & Deployment
- **Containerization**: Docker
- **Deployment Platforms**: Netlify, Vercel, Render, AWS
- **Config Management**: Environment variables with python-dotenv

## 📁 Project Structure

```
MediCore/
├── frontend/                    # React + TypeScript frontend
│   ├── src/
│   │   ├── components/         # Reusable UI components
│   │   │   ├── ui/            # shadcn/ui components
│   │   │   ├── dashboard/     # Dashboard-specific components
│   │   │   ├── ai/            # AI-related components
│   │   │   └── sahayak/       # SahayakAI components
│   │   ├── pages/             # Page components (routing)
│   │   ├── services/          # API integration
│   │   ├── hooks/             # Custom React hooks
│   │   ├── lib/               # Utility functions
│   │   ├── data/              # Static data (schemes, etc.)
│   │   ├── App.tsx            # Root component
│   │   └── main.tsx           # Entry point
│   ├── public/                # Static assets
│   ├── vite.config.ts         # Vite configuration
│   ├── tailwind.config.ts     # Tailwind CSS config
│   ├── tsconfig.json          # TypeScript config
│   ├── package.json           # Frontend dependencies
│   └── Dockerfile.aws         # AWS deployment config
│
├── backend/                    # FastAPI backend entry point
│   ├── main.py               # Application bootstrap
│   └── requirements.txt       # Python dependencies
│
├── Hackathon/                 # Primary backend implementation
│   ├── backend/
│   │   ├── main.py          # FastAPI app and router setup
│   │   ├── routers/         # Feature-specific route handlers
│   │   │   ├── users.py           # User management endpoints
│   │   │   ├── token.py           # Authentication endpoints
│   │   │   ├── coach.py           # AROMI coaching endpoints
│   │   │   ├── meals.py           # Meal plan endpoints
│   │   │   ├── workout.py         # Workout plan endpoints
│   │   │   ├── predictions.py     # Disease prediction endpoints
│   │   │   ├── progress.py        # Progress tracking endpoints
│   │   │   ├── sahayak.py         # Disability scheme endpoints
│   │   │   ├── manasmitra.py      # Mental health endpoints
│   │   │   └── __init__.py
│   │   ├── services/
│   │   │   ├── auth.py           # JWT and security utilities
│   │   │   ├── groq_service.py   # Groq AI integration
│   │   │   └── scheme_search.py  # Disability scheme search
│   │   ├── database.py           # ORM models and session management
│   │   ├── schemas.py            # Pydantic request/response models
│   │   ├── requirements.txt      # Python dependencies
│   │   └── uploads/             # User uploads directory
│   │
│   ├── src/                  # ML model training scripts
│   │   ├── image_preprocessor.py
│   │   ├── model.py
│   │   ├── train_ham10000.py     # Skin lesion model training
│   │   └── train_lungs.py        # Lung classifier training
│   │
│   ├── models/               # Pre-trained ML models
│   │   ├── skin_lesion_model.pth
│   │   └── train_models.py
│   │
│   ├── data/                 # Training data
│   │   ├── anemia.csv
│   │   ├── diabetes.csv
│   │   └── hypertension.csv
│   │
│   ├── streamlit_app.py      # Streamlit data visualization app
│   ├── Dockerfile           # Backend container config
│   ├── render.yaml          # Render deployment config
│   └── README.md            # Backend-specific documentation
│
├── deploy/                   # Deployment configurations
│   └── aws/                 # AWS-specific deployment
│
├── uploads/                  # User predictions storage
│   └── medicore_predictions/
│
├── netlify.toml             # Netlify deployment config
├── render.yaml              # Render deployment config
├── vercel.json              # Vercel deployment config
└── README.md                # This file

```

## 🚀 Installation & Setup

### Prerequisites

- **Node.js** 18+ and npm/yarn
- **Python** 3.8+
- **Git**
- **Groq API Key** (for AI features)

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd Hackathon/backend
   ```

2. **Create and activate a Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   SECRET_KEY=your_secret_key_here
   DATABASE_URL=sqlite:///./medicore.db
   CORS_ORIGINS=http://localhost:5173,http://localhost:3000
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   PORT=8002
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Create environment configuration** (if needed):
   Create `.env.local`:
   ```env
   VITE_API_URL=http://localhost:8002
   ```

## 🏃 Running the Project

### Option 1: Run Backend and Frontend Separately

**Terminal 1 - Backend:**
```bash
cd Hackathon/backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
Backend runs on: `http://localhost:8002`

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on: `http://localhost:5173`

### Option 2: Using Docker

**Build and run with Docker Compose:**
```bash
docker-compose up --build
```

### Option 3: Cloud Deployment

- **Render**: Use `render.yaml` configuration
- **Vercel**: Use `vercel.json` for frontend deployment
- **Netlify**: Use `netlify.toml` for frontend deployment
- **AWS**: Use configurations in `deploy/aws/` directory

## 🔧 Environment Variables

### Backend Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GROQ_API_KEY` | Groq API key for LLM services | `gsk_...` |
| `SECRET_KEY` | JWT signing secret | `your-secret-key` |
| `DATABASE_URL` | Database connection string | `sqlite:///./medicore.db` |
| `CORS_ORIGINS` | Allowed CORS origins (comma-separated) | `http://localhost:5173,http://localhost:3000` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration time | `30` |
| `PORT` | Server port | `8002` |

### Frontend Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API URL | `http://localhost:8002` |

## 📡 API Endpoints

### Authentication
- `POST /register` - User registration
- `POST /token` - User login
- `POST /forgot-password` - Password recovery

### User Management
- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update user profile

### AI Coach (AROMI)
- `POST /coach/chat` - Coach chat interface
- `POST /meals/generate` - Generate meal plans
- `POST /workout/generate` - Generate workout plans

### Predictions & Diagnosis
- `POST /predictions/predict` - Predict disease from clinical data
- `POST /predictions/image-diagnosis` - Diagnose from medical images

### SahayakAI
- `POST /sahayak/search` - Search disability schemes
- `GET /sahayak/schemes` - Get all schemes

### Mental Health (ManasMitra)
- `POST /manasmitra/checkin` - Mental health check-in
- `GET /manasmitra/summary` - Get wellness summary

### Progress & Activity
- `GET /progress/dashboard` - Get progress dashboard
- `POST /activity/log` - Log activity

### Health Check
- `GET /health` - Backend health status

For complete API documentation, access the interactive docs at:
- **Swagger UI**: `http://localhost:8002/docs`
- **ReDoc**: `http://localhost:8002/redoc`

## 💻 Development

### Frontend Development
- **Start dev server**: `npm run dev`
- **Build for production**: `npm run build`
- **Run tests**: `npm run test`
- **Run tests in watch mode**: `npm run test:watch`
- **Lint code**: `npm run lint`
- **Preview production build**: `npm run preview`

### Backend Development
- **Start development server**: `python main.py`
- **Run database migrations**: `python database.py`
- **Train ML models**: `python Hackathon/src/train_ham10000.py`
- **View Streamlit dashboard**: `streamlit run Hackathon/streamlit_app.py`

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/YourFeature`
3. **Commit your changes**: `git commit -m 'Add YourFeature'`
4. **Push to the branch**: `git push origin feature/YourFeature`
5. **Open a Pull Request**

### Code Standards
- Follow PEP 8 for Python code
- Use TypeScript for React components
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for healthcare accessibility and wellness
- Powered by Groq API for AI capabilities
- UI components from shadcn/ui and Radix UI
- Community contributions and feedback

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review API docs at `/docs` endpoint

---

**Last Updated**: May 2026  
**Version**: 1.0.0
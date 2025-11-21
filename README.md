# FreightFlowAI Backend

Backend service for the FreightFlowAI logistics platform. Built with FastAPI, SQLAlchemy, and Docker.

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.12+ (for local development)

### 🐳 Running with Docker (Recommended)
The easiest way to run the backend is with Docker.

1. **Create a `.env` file**
   ```bash
   cp .env.example .env
   ```
   Ensure `DATABASE_URL` and `SECRET_KEY` are set.

2. **Build and Run**
   ```bash
   docker build -t freightflow-backend .
   docker run --env-file .env -p 8000:8000 freightflow-backend
   ```

3. **Access the API**
   - API: http://localhost:8000
   - Docs (Swagger UI): http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

---

## 🛠️ Local Development

1. **Create Virtual Environment**
   ```bash
   python -m venv backend_venv
   source backend_venv/bin/activate  # Windows: backend_venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🧪 Testing

We use `pytest` for testing.

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v
```

**Test Structure:**
- `tests/conftest.py`: Fixtures (DB, Client)
- `tests/test_trips.py`: Tests for Trip CRUD
- `tests/test_documents.py`: Tests for Document Uploads (Mocked)

---

## 📂 Project Structure

```
FreightFlowAI_backend/
├── app/
│   ├── models/       # SQLAlchemy Database Models
│   ├── routers/      # FastAPI Routes (Endpoints)
│   ├── schemas/      # Pydantic Schemas (Validation)
│   ├── services/     # Business Logic (OCR, Uploads)
│   ├── config.py     # Configuration & Env Vars
│   ├── db.py         # Database Connection
│   └── main.py       # App Entrypoint
├── tests/            # Pytest Tests
├── local_files/      # Local storage for uploads (Ignored by Git)
├── .env              # Secrets (Ignored by Git)
├── Dockerfile
└── requirements.txt
```

## 🔑 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///./freightflow.db` |
| `SECRET_KEY` | Secret for security | `change_me` |

## 📝 API Overview

### Trips
- `POST /trips/`: Create a new trip
- `GET /trips/`: List all trips
- `GET /trips/{id}`: Get trip details
- `PATCH /trips/{id}`: Update trip status

### Documents
- `POST /trips/{id}/documents`: Upload a document (BOL, POD, etc.)
- `GET /trips/{id}/documents`: List documents for a trip

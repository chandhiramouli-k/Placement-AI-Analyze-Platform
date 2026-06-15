from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.student_routes import router as student_router
from api.analysis_routes import router as analysis_router

app = FastAPI(
    title="Placement Readiness AI Platform",
    version="1.0.0"
)

# ======================
# CORS (IMPORTANT for Streamlit)
# ======================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================
# ROUTES
# ======================
app.include_router(
    student_router,
    prefix="/students",
    tags=["Students"]
)

app.include_router(
    analysis_router,
    prefix="/analysis",
    tags=["AI Analysis"]
)

# ======================
# ROOT
# ======================
@app.get("/")
def home():
    return {
        "message": "Placement Readiness AI Platform Running"
    }
from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware

# Import your routers here
# from .api.routes import users_router, log_router, insights_router

app = FastAPI(
    title="Smart Diabetes Companion API",
    description="API for managing diabetes data, insights, and proactive nudges.",
    version="1.0.0",
)

# CORS Middleware to allow requests from the frontend
origins = [
    "http://localhost:3000", # Assuming frontend runs on 3000
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
# app.include_router(users_router, prefix="/users")
# app.include_router(log_router, prefix="/log")
# app.include_router(insights_router, prefix="/insights")

# Placeholder for ML model serving route - ideally this would be in ml_service
@app.get("/predict/glucose")
def predict_glucose():
    return {"message": "Glucose prediction endpoint - integrate ML service here"}

# Basic health check
@app.get("/")
def read_root():
    return {"status": "API is running"}

if __name__ == "__main__":
    # For development purposes, use uvicorn directly
    # In production, use a proper ASGI server like Gunicorn with Uvicorn worker
    run(app, host="0.0.0.0", port=8000)

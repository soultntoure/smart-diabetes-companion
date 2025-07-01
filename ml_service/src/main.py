from fastapi import FastAPI
from uvicorn import run
from .api.routes import prediction_router

app = FastAPI(
    title="Diabetes ML Service",
    description="Provides AI-powered insights and predictions for diabetes management.",
    version="1.0.0",
)

# Include ML-specific routers
app.include_router(prediction_router, prefix="/ml")

@app.get("/ml/health")
def ml_health_check():
    return {"status": "ML Service is healthy"}

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8001) # ML service on a different port

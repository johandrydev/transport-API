from fastapi import FastAPI
from api.routes import router

# Create FastAPI app instance
app = FastAPI()

# Include API routes
app.include_router(router, prefix="/api/v1")

# Root endpoint
@app.post("/", tags=["Health Check"])
async def health_check():
    return {"status": "OK", "message": "Transport Service API is running"}

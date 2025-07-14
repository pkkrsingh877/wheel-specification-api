from fastapi import FastAPI, Query

from routes.wheel_form import router as wheel_form_router

app = FastAPI(
    title="Wheel Specification API",
    version="1.0.0"
)

app.include_router(wheel_form_router, prefix="/api/forms", tags=["Wheel Specifications"])


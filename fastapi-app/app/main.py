from fastapi import FastAPI

from app.api.routes import router as ai_router
from app.core.config import settings

app = FastAPI(title=settings.service_name)
app.include_router(ai_router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from app.api import windows
from app.models.base  import Base
from app.db.session import engine
from app.core.config import conf_settings


def get_application() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    app = FastAPI()
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=conf_settings.ALLOWED_ORIGINS,
        allow_credentials=conf_settings.ALLOW_CREDENTIALS,
        allow_methods=conf_settings.ALLOW_METHODS,
        allow_headers=conf_settings.ALLOW_HEADERS,
    )
    
    app.include_router(windows.router, prefix="/windows")
    logger.add("log_api.log", rotation="100 MB")
    return app

app = get_application()

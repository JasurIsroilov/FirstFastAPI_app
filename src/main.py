from fastapi import FastAPI

from config import Settings

from auth.router import router as auth_router
from users.router import router as users_router
from roles.router import router as roles_router


app = FastAPI(
    title="First App",
    docs_url=f"/{Settings.CONFIG_URL}/docs",
    redoc_url=f"/{Settings.CONFIG_URL}/redoc"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(roles_router)

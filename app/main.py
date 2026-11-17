from fastapi import FastAPI
from app.routers import user, login

app = FastAPI(title="Социальная сеть - OTUS")

app.include_router(user.router)
app.include_router(login.router)

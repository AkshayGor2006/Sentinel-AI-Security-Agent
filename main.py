from fastapi import FastAPI

from routes import repo


app = FastAPI()


app.include_router(
    repo.router
)
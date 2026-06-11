from fastapi import FastAPI

from routes import repo


app = FastAPI()   #creates ur backend application 


app.include_router(                         #connects ur api routes
    repo.router
)
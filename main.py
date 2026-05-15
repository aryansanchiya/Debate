from fastapi import FastAPI
from db.database import Base, engine
from api.user_api import router as user_router
from api.debate_api import router as debate_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(debate_router)

@app.get("/")
def root():
    return {
        "message": "Debate Platform Running"
    }
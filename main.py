from fastapi import FastAPI
from routes.Message import router as MessageRouter

app = FastAPI()

app.include_router(MessageRouter)
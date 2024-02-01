from fastapi import FastAPI
from routes.Message import router as MessageRouter
from routes.User import router as UserRouter
from routes.Thread import router as ThreadRouter

app = FastAPI()

app.include_router(MessageRouter)
app.include_router(UserRouter)
app.include_router(ThreadRouter)
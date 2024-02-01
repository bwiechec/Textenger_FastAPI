from fastapi import FastAPI
from routes.Message import router as MessageRouter
from routes.User import router as UserRouter
from routes.Thread import router as ThreadRouter
from fastapi import FastAPI, __version__
from fastapi.responses import HTMLResponse
from fastapi import redirect_to

app = FastAPI()

app.include_router(MessageRouter)
app.include_router(UserRouter)
app.include_router(ThreadRouter)

@app.get("/", include_in_schema=False)
async def root():
    return redirect_to("/redoc")

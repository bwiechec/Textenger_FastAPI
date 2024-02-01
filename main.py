from fastapi import FastAPI, Request
from routes.Message import router as MessageRouter
from routes.User import router as UserRouter
from routes.Thread import router as ThreadRouter
from fastapi import FastAPI, __version__
from fastapi.responses import RedirectResponse

app = FastAPI(title="Textenger", description="Textenger API", version="0.1.0")

app.include_router(MessageRouter)
app.include_router(UserRouter)
app.include_router(ThreadRouter)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs", status_code=302)

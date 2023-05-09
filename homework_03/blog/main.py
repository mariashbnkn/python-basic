import uvicorn
from fastapi import FastAPI

from views import router as pings_router

app = FastAPI(
    redoc_url=None,
)
app.include_router(
    pings_router,
    prefix="/ping",
)


@app.get("/")
def index():
    return {
        "message": "hi-hi",
    }


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )
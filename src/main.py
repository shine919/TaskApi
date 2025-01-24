from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from src.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    default_response_class=ORJSONResponse,
)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

from fastapi import FastAPI
from poor import poor as poor_router

app = FastAPI()

app.include_router(poor_router, prefix="/poor", tags=["Poor"])


@app.get("/")
def root():
    return {"message": "Hello World!"}

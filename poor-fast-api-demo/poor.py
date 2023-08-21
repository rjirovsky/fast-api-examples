from fastapi import APIRouter

poor = APIRouter()
@poor.get("/")
def root():
  return {"message": "Poor hello"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from config import FRONTEND_HOST, FRONTEND_PORT, TEST_IP

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"http://{FRONTEND_HOST}:{FRONTEND_PORT}",
        f"http://{TEST_IP}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"Welcome to": "API!"}

app.include_router(router)
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="WebBrain API")

from services.backend.app.api.v1 import scraper
from services.backend.app.api.v1 import history
# ✅ Include your router here
app.include_router(scraper.router)
app.include_router(history.router)
# Enable CORS (so frontend can call API later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "WebBrain backend is running!"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.leads import router as leads_router
from app.routers.scan import router as scan_router

app = FastAPI(title="LeadFlow AI API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(leads_router)
app.include_router(scan_router)

@app.get("/health")
async def health():
    return {"ok": True, "service": "leadflow-api", "version": app.version}

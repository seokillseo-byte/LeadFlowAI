from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["scan"])

@router.post("/scan")
async def scan():
    return {"ok": True, "message": "Scan job queued"}

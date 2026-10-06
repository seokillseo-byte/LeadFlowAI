from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Lead
from app.db.session import get_session
from app.services.leads import build_lead_service

router = APIRouter(prefix="/api/leads", tags=["leads"])

class LeadResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    post_id: int
    campaign_id: int
    score: int | None = None
    intent: str | None = None
    fit: str | None = None
    need: str | None = None
    confidence: float | None = None
    status: str | None = None

def response(lead: Lead) -> LeadResponse:
    return LeadResponse.model_validate(lead)

@router.get("", response_model=list[LeadResponse])
async def list_leads(session: AsyncSession = Depends(get_session)):
    return [response(x) for x in await build_lead_service(session).list_leads()]

@router.get("/{lead_id}", response_model=LeadResponse)
async def get_lead(lead_id: int, session: AsyncSession = Depends(get_session)):
    lead = await build_lead_service(session)._repository.get(lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail={"code": "lead_not_found", "message": "Lead not found"})
    return response(lead)

@router.post("/{lead_id}/approve", response_model=LeadResponse)
async def approve_lead(lead_id: int, session: AsyncSession = Depends(get_session)):
    lead = await build_lead_service(session).approve(lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail={"code": "lead_not_found", "message": "Lead not found"})
    return response(lead)

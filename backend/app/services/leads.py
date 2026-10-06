from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.lead import LeadRepository, SqlAlchemyLeadRepository

class LeadService:
    def __init__(self, repository: LeadRepository):
        self._repository = repository

    async def list_leads(self):
        return await self._repository.list()

    async def get(self, lead_id: int):
        return await self._repository.get(lead_id)

    async def approve(self, lead_id: int):
        return await self._repository.approve(lead_id)

def build_lead_service(session: AsyncSession) -> LeadService:
    return LeadService(SqlAlchemyLeadRepository(session))

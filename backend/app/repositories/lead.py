from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Lead

class LeadRepository(ABC):
    @abstractmethod
    async def list(self) -> list[Lead]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, lead_id: int) -> Lead | None:
        raise NotImplementedError

    @abstractmethod
    async def approve(self, lead_id: int) -> Lead | None:
        raise NotImplementedError

class SqlAlchemyLeadRepository(LeadRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def list(self) -> list[Lead]:
        result = await self._session.execute(select(Lead).order_by(Lead.id))
        return list(result.scalars().all())

    async def get(self, lead_id: int) -> Lead | None:
        return await self._session.get(Lead, lead_id)

    async def approve(self, lead_id: int) -> Lead | None:
        lead = await self.get(lead_id)
        if lead is None:
            return None
        lead.status = "approved"
        await self._session.commit()
        await self._session.refresh(lead)
        return lead

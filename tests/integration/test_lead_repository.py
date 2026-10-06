from datetime import datetime, timezone

import pytest
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from backend.app.db.models import Base, Campaign, Lead, Post
from backend.app.repositories.lead import SqlAlchemyLeadRepository

@pytest.mark.asyncio
async def test_lead_repository_list_and_approve():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    session_factory = async_sessionmaker(engine, expire_on_commit=False)
    async with session_factory() as session:
        now = datetime.now(timezone.utc)
        campaign = Campaign(name="fixture", created_at=now, updated_at=now)
        session.add(campaign)
        await session.flush()

        post = Post(provider="fixture", external_id="post-1", created_at=now)
        session.add(post)
        await session.flush()

        lead = Lead(post_id=post.id, campaign_id=campaign.id, score=10, status="new", created_at=now, updated_at=now)
        session.add(lead)
        await session.commit()

        repository = SqlAlchemyLeadRepository(session)
        assert len(await repository.list()) == 1
        approved = await repository.approve(lead.id)
        assert approved is not None
        assert approved.status == "approved"

    await engine.dispose()

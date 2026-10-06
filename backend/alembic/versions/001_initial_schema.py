"""Initial canonical SQLite schema.

Revision ID: 001_initial_schema
Revises:
Create Date: 2026-10-06
"""
from alembic import op
from app.db.models import Base

revision = "001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    bind = op.get_bind()
    Base.metadata.create_all(bind=bind)

def downgrade() -> None:
    bind = op.get_bind()
    Base.metadata.drop_all(bind=bind)

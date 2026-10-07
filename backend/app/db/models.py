from datetime import datetime
from typing import Any
from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, Text, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

def pk() -> Mapped[int]:
    return mapped_column(Integer, primary_key=True, autoincrement=True)

def created_updated():
    return (mapped_column(DateTime(timezone=True), nullable=False), mapped_column(DateTime(timezone=True), nullable=False))

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = pk()
    display_name: Mapped[str | None] = mapped_column(String(255))
    email: Mapped[str | None] = mapped_column(String(320))
    plan: Mapped[str | None] = mapped_column(String(64))
    created_at, updated_at = created_updated()

class ProviderAccount(Base):
    __tablename__ = "provider_accounts"
    id: Mapped[int] = pk()
    provider: Mapped[str] = mapped_column(String(64), nullable=False)
    external_account_id: Mapped[str | None] = mapped_column(String(255))
    display_name: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str | None] = mapped_column(String(64))
    capabilities_json: Mapped[dict[str, Any] | None] = mapped_column(JSON)
    created_at, updated_at = created_updated()

class Campaign(Base):
    __tablename__ = "campaigns"
    id: Mapped[int] = pk()
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str | None] = mapped_column(String(64))
    schedule_json: Mapped[dict[str, Any] | None] = mapped_column(JSON)
    provider_account_id: Mapped[int | None] = mapped_column(ForeignKey("provider_accounts.id"))
    created_at, updated_at = created_updated()

class KeywordRule(Base):
    __tablename__ = "keyword_rules"
    id: Mapped[int] = pk()
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaigns.id"), nullable=False)
    rule_type: Mapped[str | None] = mapped_column(String(64))
    term: Mapped[str] = mapped_column(String(255), nullable=False)
    match_mode: Mapped[str | None] = mapped_column(String(64))
    enabled: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

class SourceTarget(Base):
    __tablename__ = "source_targets"
    id: Mapped[int] = pk()
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaigns.id"), nullable=False)
    target_type: Mapped[str | None] = mapped_column(String(64))
    external_id: Mapped[str | None] = mapped_column(String(255))
    display_name: Mapped[str | None] = mapped_column(String(255))
    enabled: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = pk()
    provider: Mapped[str] = mapped_column(String(64), nullable=False)
    external_id: Mapped[str] = mapped_column(String(255), nullable=False)
    source_target_id: Mapped[int | None] = mapped_column(ForeignKey("source_targets.id"))
    author_external_id: Mapped[str | None] = mapped_column(String(255))
    author_name: Mapped[str | None] = mapped_column(String(255))
    content: Mapped[str | None] = mapped_column(Text)
    permalink: Mapped[str | None] = mapped_column(String(2048))
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    raw_hash: Mapped[str | None] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

class Lead(Base):
    __tablename__ = "leads"
    id: Mapped[int] = pk()
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaigns.id"), nullable=False)
    score: Mapped[int | None] = mapped_column(Integer)
    intent: Mapped[str | None] = mapped_column(String(64))
    fit: Mapped[str | None] = mapped_column(String(64))
    need: Mapped[str | None] = mapped_column(String(255))
    confidence: Mapped[float | None]
    status: Mapped[str | None] = mapped_column(String(64))
    created_at, updated_at = created_updated()

class AIAnalysis(Base):
    __tablename__ = "ai_analyses"
    id: Mapped[int] = pk()
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"), nullable=False)
    model: Mapped[str | None] = mapped_column(String(255))
    prompt_version: Mapped[str | None] = mapped_column(String(128))
    result_json: Mapped[dict[str, Any] | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

class Template(Base):
    __tablename__ = "templates"
    id: Mapped[int] = pk()
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str | None] = mapped_column(Text)
    category: Mapped[str | None] = mapped_column(String(64))
    variables_json: Mapped[dict[str, Any] | None] = mapped_column(JSON)
    active: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at, updated_at = created_updated()

class ReplySuggestion(Base):
    __tablename__ = "reply_suggestions"
    id: Mapped[int] = pk()
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"), nullable=False)
    template_id: Mapped[int | None] = mapped_column(ForeignKey("templates.id"))
    content: Mapped[str | None] = mapped_column(Text)
    model: Mapped[str | None] = mapped_column(String(255))
    confidence: Mapped[float | None]
    status: Mapped[str | None] = mapped_column(String(64))
    created_at, updated_at = created_updated()

class Approval(Base):
    __tablename__ = "approvals"
    id: Mapped[int] = pk()
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"), nullable=False)
    action_type: Mapped[str] = mapped_column(String(64), nullable=False)
    decision: Mapped[str | None] = mapped_column(String(64))
    approved_by: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    approved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    reason: Mapped[str | None] = mapped_column(Text)

class Action(Base):
    __tablename__ = "actions"
    id: Mapped[int] = pk()
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"), nullable=False)
    action_type: Mapped[str] = mapped_column(String(64), nullable=False)
    provider_account_id: Mapped[int | None] = mapped_column(ForeignKey("provider_accounts.id"))
    status: Mapped[str | None] = mapped_column(String(64))
    idempotency_key: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    created_at, updated_at = created_updated()

class ActionAttempt(Base):
    __tablename__ = "action_attempts"
    id: Mapped[int] = pk()
    action_id: Mapped[int] = mapped_column(ForeignKey("actions.id"), nullable=False)
    attempt_number: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str | None] = mapped_column(String(64))
    provider_request_id: Mapped[str | None] = mapped_column(String(255))
    error_code: Mapped[str | None] = mapped_column(String(128))
    error_message: Mapped[str | None] = mapped_column(Text)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

class AuditEvent(Base):
    __tablename__ = "audit_events"
    id: Mapped[int] = pk()
    actor_type: Mapped[str | None] = mapped_column(String(64))
    actor_id: Mapped[str | None] = mapped_column(String(255))
    event_type: Mapped[str] = mapped_column(String(128), nullable=False)
    entity_type: Mapped[str | None] = mapped_column(String(64))
    entity_id: Mapped[str | None] = mapped_column(String(255))
    metadata_json: Mapped[dict[str, Any] | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

class Notification(Base):
    __tablename__ = "notifications"
    id: Mapped[int] = pk()
    type: Mapped[str] = mapped_column(String(64), nullable=False)
    severity: Mapped[str | None] = mapped_column(String(64))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str | None] = mapped_column(Text)
    read_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

Index("ix_posts_provider_external", Post.provider, Post.external_id, unique=True)
Index("ix_leads_campaign_status_score", Lead.campaign_id, Lead.status, Lead.score)
Index("ix_keyword_rules_campaign_enabled", KeywordRule.campaign_id, KeywordRule.enabled)
Index("ix_actions_status_created_at", Action.status, Action.created_at)
Index("ix_audit_events_entity_created_at", AuditEvent.entity_type, AuditEvent.entity_id, AuditEvent.created_at)
Index("ix_notifications_read_created_at", Notification.read_at, Notification.created_at)

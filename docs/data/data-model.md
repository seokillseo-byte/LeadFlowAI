# Data Model Blueprint

The MVP uses SQLite behind a repository/data-access layer. Schema changes must be migration-based.

## Tables

### users
id, display_name, email, plan, created_at, updated_at

### provider_accounts
id, provider, external_account_id, display_name, status, capabilities_json, created_at, updated_at

### campaigns
id, name, status, schedule_json, provider_account_id, created_at, updated_at

### keyword_rules
id, campaign_id, rule_type, term, match_mode, enabled, created_at

### source_targets
id, campaign_id, target_type, external_id, display_name, enabled

### posts
id, provider, external_id, source_target_id, author_external_id, author_name, content, permalink, published_at, raw_hash, created_at

### leads
id, post_id, campaign_id, score, intent, fit, need, confidence, status, created_at, updated_at

### ai_analyses
id, lead_id, model, prompt_version, result_json, created_at

### reply_suggestions
id, lead_id, template_id, content, model, confidence, status, created_at, updated_at

### approvals
id, lead_id, action_type, decision, approved_by, approved_at, reason

### actions
id, lead_id, action_type, provider_account_id, status, idempotency_key, created_at, updated_at

### action_attempts
id, action_id, attempt_number, status, provider_request_id, error_code, error_message, started_at, completed_at

### templates
id, name, content, category, variables_json, active, version, created_at, updated_at

### audit_events
id, actor_type, actor_id, event_type, entity_type, entity_id, metadata_json, created_at

### notifications
id, type, severity, title, body, read_at, created_at

## Indexes

At minimum index:
- posts(provider, external_id)
- leads(campaign_id, status, score)
- keyword_rules(campaign_id, enabled)
- actions(status, created_at)
- audit_events(entity_type, entity_id, created_at)
- notifications(read_at, created_at)

## Migration rule

Every schema change gets a migration and a rollback/forward-compatibility note.

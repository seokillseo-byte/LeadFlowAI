# Data Flow & State Transitions

## Lead lifecycle

```
DISCOVERED
   ↓
NORMALIZED
   ↓
MATCHED
   ↓
AI_ANALYZED
   ↓
QUEUED_FOR_REVIEW
   ├──────────────→ REJECTED
   ├──────────────→ SNOOZED
   ├──────────────→ NOT_RELEVANT
   ↓
APPROVED
   ↓
ACTION_QUEUED
   ↓
EXECUTING
   ├──────────────→ FAILED
   └──────────────→ COMPLETED
                         ↓
                      TRACKED
```

## Core entities

- Workspace/User
- ProviderAccount
- Campaign
- KeywordRule
- SourceTarget
- Post
- Lead
- AIAnalysis
- ReplySuggestion
- Approval
- Action
- ActionAttempt
- AuditEvent
- Notification
- Template
- AnalyticsEvent

## Idempotency

External object IDs and action keys must be used to prevent duplicate processing. Re-running a scan must not create duplicate leads or duplicate outbound actions.

## Approval invariant

No outbound comment/message may execute unless the action has a valid approval record associated with the current user/session context.

## Pause invariant

When the global or campaign kill switch is active, discovery may finish safely but new outbound execution must not begin.

## Audit invariant

Creation, approval, rejection, execution, failure, provider permission changes and safety-control changes must be auditable.

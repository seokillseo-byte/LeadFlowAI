# Security, Safety & Operational Controls

## Required controls

- No password or cookie/session-token collection.
- No CAPTCHA bypass.
- No stealth browser automation.
- No scraping-bypass techniques.
- Use supported official Meta APIs and permissions.
- Store secrets outside source control.
- Redact access tokens and sensitive provider payloads from logs.
- Human approval is required for outbound actions.
- Rate limits apply per provider account and action type.
- Deduplication is mandatory.
- Global pause/kill switch must be visible.
- Campaign-level pause must stop new work.
- Failed provider calls must not silently retry forever.

## Audit events

At minimum record:
- provider connected/disconnected
- permission/capability change
- campaign created/paused/resumed
- scan started/completed/failed
- lead created/updated
- AI analysis completed
- suggestion edited
- approval/rejection
- outbound action attempted/completed/failed
- rate limit reached
- kill switch enabled/disabled

## Data protection

Use least privilege. Keep tokens in secure OS-appropriate storage where feasible; do not put provider secrets in the React bundle or SQLite plaintext unless the design explicitly accepts that risk.

## Safety boundary

The UI may show an action as "suggested", "ready for approval", or "approved". It must never imply that AI approval equals user approval.

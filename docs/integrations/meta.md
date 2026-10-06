# Meta Integration Blueprint

## Boundary

All Meta-specific behavior lives behind the provider adapter.

## Requirements

- Official Meta APIs only
- OAuth and supported permissions
- Capability/permission checks
- Rate-limit awareness
- Clear error states
- Audit every outbound action

## Explicitly prohibited implementation patterns

- Cookie/session-token extraction
- CAPTCHA bypass
- Stealth browser automation
- Scraping that bypasses platform controls
- Bulk unsolicited outreach

## Provider responsibilities

The provider layer should normalize external objects into internal domain models and expose explicit capabilities for discovery and permitted actions.

# ADR-003: Meta Integration

## Status
Accepted

## Decision
Integrate Facebook/Meta through an explicit provider adapter using official APIs and supported permissions.

## Why
- Maintainable integration boundary
- Clear capability checks
- Better error/rate-limit handling
- Avoid platform-control bypass patterns

## Consequence
No cookie/session scraping, CAPTCHA bypass, stealth automation, or unsolicited bulk outreach. Outbound actions pass through an approval boundary.

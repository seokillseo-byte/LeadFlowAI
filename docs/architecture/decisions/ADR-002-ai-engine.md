# ADR-002: AI Engine Boundary

## Status
Accepted

## Decision
Keep AI operations behind backend service boundaries rather than calling models directly from the desktop renderer.

## Why
- Protect secrets
- Centralize prompts and schemas
- Make model providers replaceable
- Enable logging and evaluation
- Keep UI independent from model implementation

## Consequence
The backend owns structured AI requests/results. The UI consumes stable domain objects.

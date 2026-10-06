# Implementation Map

This document maps the blueprint to the codebase.

## Frontend

`src/App.tsx`
- Application shell and route-level composition during MVP.

`src/styles.css`
- Global design tokens and visual system.

As the app grows, split into:
- components/
- pages/
- features/
- hooks/
- api/
- types/

## Backend

`backend/app/main.py`
- FastAPI application entry point.

Planned domain modules:
- api/
- models/
- repositories/
- services/
- providers/
- jobs/
- safety/
- analytics/

## Provider

`backend/app/providers/meta.py`
- Only provider boundary.
- Must remain independent from UI and domain services.

## Rule

Do not add business logic directly to React components or provider adapters. Put business rules in backend domain services and expose stable API contracts.

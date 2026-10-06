# ADR-001: Desktop Stack

## Status
Accepted

## Decision
Use Electron + React + TypeScript for the Windows desktop application.

## Why
- Mature Windows desktop packaging
- React ecosystem for rapid UI development
- TypeScript for maintainability
- Clear separation between renderer and backend
- Existing team familiarity

## Consequence
Native OS integration belongs in Electron's main/preload boundary. Business logic should remain outside the renderer.

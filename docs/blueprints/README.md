# LeadFlow AI Blueprints

These SVG files are version-controlled visual source-of-truth artifacts.

## Master blueprints

- `leadflow-ai-architecture.svg` — detailed system architecture, data flow, safety boundary and implementation modules.
- `leadflow-ai-dashboard.svg` — master product UI reference based on the approved dashboard design.

## Supporting specs

Visuals are not the only source of truth. Use them together with:
- `docs/product/requirements.md`
- `docs/product/feature-matrix.md`
- `docs/architecture/architecture.md`
- `docs/architecture/detailed-architecture.md`
- `docs/architecture/data-flow.md`
- `docs/ui/design-system.md`
- screen-specific UI specs under `docs/ui/`

## Change rule

If implementation intentionally deviates from a blueprint, update the relevant spec and blueprint in the same change set. Do not silently drift from the design.

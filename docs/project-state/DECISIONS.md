# LeadFlow AI — Project Decisions

## Durable operating decisions

### D-001 — GitHub is project memory

The repository is the source of truth across ChatGPT accounts. Important project state must not live only in chat.

### D-002 — Task queue controls WHAT

Agents may decide implementation details within their ownership, but the project queue controls which work is done next.

### D-003 — Agents may continue, but may not cross human gates

Agents may audit, implement, test, self-review, update PRs and project state, and select the next queue task. They must stop before merge, major architecture/contract changes, external authorization, or real outbound execution.

### D-004 — No speculative work

Agents must not create unrelated improvements merely because they notice them. Discovered issues should be fixed only when required for the current task or recorded as a future task.

### D-005 — Evidence over claims

PASS means the command or GitHub check was actually observed. NOT VERIFIED means it was not observed. Agents must never convert absence of evidence into PASS.

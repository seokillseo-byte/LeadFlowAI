# Contributing to LeadFlow AI

## Workflow

1. Pick or create a GitHub Issue.
2. Read the relevant blueprint/spec under docs/.
3. Create a focused branch.
4. Implement the smallest complete change.
5. Run validation locally.
6. Open a Pull Request with the issue reference.
7. Request review from another team member.
8. Merge only after CI and review pass.

## Branch naming

Use:
- feature/<short-name>
- fix/<short-name>
- refactor/<short-name>
- docs/<short-name>

## Commit style

Prefer:
- feat: ...
- fix: ...
- refactor: ...
- docs: ...
- test: ...
- chore: ...

## AI-assisted development

Team members may use ChatGPT or other coding agents. The repository is the shared source of truth. Do not rely on private chat history for architectural or product decisions.

Every AI-assisted change must still be reviewed by a human before merge.

## Secrets

Never commit:
- API keys
- OAuth client secrets
- access tokens
- passwords
- cookies/session data
- production credentials

Use .env locally and keep only .env.example in the repository.

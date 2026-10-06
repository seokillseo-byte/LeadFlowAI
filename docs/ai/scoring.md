# AI Scoring Blueprint

## Purpose

Rank discovered posts/leads by commercial intent so users can prioritize review.

## Target output

- intent
- lead_score: 0–100
- fit classification
- extracted need
- confidence
- suggested reply

## Principles

AI output is advisory. The score does not authorize outbound actions.

## Future model contract

The backend should expose a stable structured result so the model provider can change without changing the rest of the application.

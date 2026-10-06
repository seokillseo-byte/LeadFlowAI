# Prompt Strategy

## Goals
Prompts should produce consistent structured outputs and minimize unsupported assumptions.

## Rules
- Give the model normalized source content and relevant campaign context.
- Ask for structured JSON matching a versioned schema.
- Separate classification from generation where practical.
- Never ask the model to perform external actions.
- Include uncertainty/confidence.
- Preserve the original source text for auditability.

## Evaluation
Maintain representative test cases for high-intent, low-intent, ambiguous, spam and out-of-scope posts.

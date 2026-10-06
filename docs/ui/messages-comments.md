# Messages & Comments UI Specification

## Purpose
Centralize outbound actions that have passed the human approval boundary.

## Sections
- Pending approval
- Approved / queued
- Completed
- Failed
- Cancelled

## Action detail
- Original post/context
- Lead score and AI reasoning
- Proposed content
- Edited content
- Target
- Provider/account
- Approval actor/time
- Execution status
- Provider request ID where safe

## Safety
No row can execute merely because a suggestion exists. Execution requires a server-side approval record and a valid provider capability.

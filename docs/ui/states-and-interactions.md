# UI States & Interaction Contract

Every major screen must support:

## Loading
Use skeletons or progress indicators without blocking unrelated navigation.

## Empty
Explain why there is no data and give the next useful action.

## Error
Show human-readable error, safe technical detail, retry action and support/correlation ID where available.

## Permission
Explain what capability is missing and provide the supported connection/settings path.

## Paused
Show whether pause is global or campaign-specific and what work is affected.

## Approval
Use explicit states: Suggested → Awaiting approval → Approved → Executing → Completed/Failed.

## Destructive actions
Require confirmation and explain consequences.

## Responsive desktop behavior
The primary target is Windows desktop. At smaller window sizes, preserve navigation and critical approval actions before decorative content.

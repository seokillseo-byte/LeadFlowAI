# Campaigns UI Specification

## Purpose
Configure what LeadFlow AI watches and when it operates.

## Screen
- Campaign list
- Status: running/paused/error
- Schedule
- Connected provider account
- Source targets
- Keyword set
- Lead threshold
- Reply template
- Notification settings
- Last scan / next scan

## Actions
- Create
- Edit
- Duplicate
- Pause
- Resume
- Delete with confirmation
- Open Lead Inbox filtered to campaign

## Safety
Pausing a campaign prevents new discovery work and outbound execution for that campaign. Existing approved actions must still obey the global safety state.

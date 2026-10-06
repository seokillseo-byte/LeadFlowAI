# Dashboard UI Specification

## Master reference
Use `docs/blueprints/leadflow-ai-dashboard.svg`.

## Header
- Running/paused system status
- Scan schedule
- Notifications
- User/profile/plan
- Window controls remain native to the desktop shell

## KPI row
Four primary cards:
1. Posts scanned
2. Potential leads
3. Comments sent
4. Messages sent

Each card includes value, period comparison and a compact visual/icon.

## Analytics
### Seven-day performance
Show time series for:
- posts scanned
- leads
- comments
- messages

### Conversion overview
Show:
- lead → customer conversion rate
- qualified leads
- replied
- consulted
- customers

## Lead Inbox preview
Must include:
- tabs for pending/processed/skipped
- campaign filter
- search
- filter control
- checkbox selection
- post preview
- source
- author
- score badge
- status chip
- open/review action

## Right rail
### Recent activity
Show lead discovery, comments/messages, warnings and timestamps.

### AI Assistant
Show:
- assistant identity/status
- explanation that the text is a suggestion
- contextual reply preview
- Copy
- Use in review flow

### Running campaigns
Show:
- campaign name
- current scan state
- source count
- enabled/paused toggle
- manage link

## Footer status bar
Show:
- Facebook connection
- account count
- Meta API status
- SQLite status
- global pause
- campaign management

## Interaction
The dashboard is an operational command center, not only an analytics page. Every metric should link to the relevant operational view where practical.

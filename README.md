# LeadFlow AI

Windows-first AI lead radar for service businesses.

## MVP
- Keyword include/exclude
- Lead Inbox with scoring
- Human approval queue
- AI reply suggestion boundary
- FastAPI backend
- Electron + React + TypeScript desktop shell
- Provider adapter for official Meta integrations

## Run backend
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

## Run desktop
npm install
npm run dev

## Build Windows
npm run build

### Safety architecture
The Meta adapter is intentionally limited to official APIs/permissions. It does not implement
cookie/session scraping, CAPTCHA bypass, stealth automation, or bulk unsolicited outreach.
Outbound actions are designed around approval, deduplication, rate limits and auditability.

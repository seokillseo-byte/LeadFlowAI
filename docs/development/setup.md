# Development Setup

## Prerequisites
- Windows 10/11
- Node.js LTS
- npm
- Python 3.11+
- Git

## Backend
~~~text
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
~~~

## Desktop
~~~text
npm install
npm run dev
~~~

## Build
~~~text
npm run build
~~~

Copy .env.example to .env for local configuration. Never commit secrets.

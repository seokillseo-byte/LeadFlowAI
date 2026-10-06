# Troubleshooting

## Backend does not start
Check Python version, virtual environment activation and dependency installation.

## Desktop does not start
Run npm install, then inspect the Vite/Electron terminal output.

## API unavailable
Confirm FastAPI is running on port 8000 and that the desktop environment points to the correct API URL.

## Meta connection fails
Check official API permissions, account capability, token configuration and provider error logs. Do not work around platform restrictions.

## AI output is malformed
Inspect the structured schema, prompt version and backend logs. Never silently execute an invalid model result.

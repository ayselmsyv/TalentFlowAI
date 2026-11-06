# TalentFlow AI — 5-hour hackathon starter

## Prerequisites
Python 3.10+, Node.js 18+ (Node 20+ recommended), npm.

## Terminal 1 — Backend
```bash
cd backend
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
API: http://localhost:8000/docs

## Terminal 2 — Frontend
```bash
cd frontend
npm install
npm run dev
```
UI: http://localhost:5173

## Optional real AI
Set environment variable `OPENAI_API_KEY` before starting backend. Optionally set `OPENAI_MODEL` (default `gpt-4o-mini`). Without an API key or if the request fails, the app uses a transparent keyword-matching demo mode. Never put API keys in frontend code.

## Demo walkthrough
1. Choose Candidate Demo > Explore Jobs > select a job.
2. Upload a fictional text-based PDF CV and click Analyze My CV.
3. Click Submit Application.
4. Switch to HR Demo > Candidate Pipeline, then change status to Interview.
5. Switch back to Candidate Demo > My Applications and click Find my applications.

## What is implemented
- React/Tailwind dashboard with HR and Candidate views
- SQLite jobs and applications
- Job creation, PDF CV upload, CV analysis, application submission and tracking
- HR candidate review and status changes
- Optional LLM analysis with keyword-based fallback

## Important limitations
- Demo role selector is **not authentication**; all API routes are public. Do not deploy to the public internet or upload real personal data.
- CV text is stored in SQLite. Use only fictional sample CVs.
- No interview video room, email notifications, signed contracts, or PDF offer generation yet.
- Keyword score measures mentions of job requirements, not true candidate fitness.
- API does not yet enforce role permissions, rate limiting, or production-grade file security.

## HR Intelligence upgrade

Choose **HR demo** and open **HR Intelligence**. The suite includes overview, candidates, comparison, bulk CV import (PDF/DOCX, up to 100 files, 5 MB each), interviews, verification status metadata, analytics, and notifications. Existing Candidate Portal and AI Resume Coach remain available.

**Security limitation:** This is a local hackathon prototype. Login does not authenticate users and HR API endpoints do not enforce authorization. Do not expose the server publicly or upload real personal, employment, or medical information. Medical documents are NOT uploaded or scored; only fictional verification references and statuses are supported. Production needs authenticated accounts, RBAC, restricted document storage, audit logs, retention policy, and security review.

**Performance limitation:** Bulk analysis is synchronous. A production system processing hundreds of CVs needs a queue/background workers and progress polling. PDF/DOCX parsing is heuristic; scanned files need OCR and structured extraction needs further improvement.

**Upgrade existing installation:** Back up your current `backend/talentflow.db`, replace `backend/main.py`, `backend/requirements.txt`, and `frontend/src/main.jsx` with the files from this ZIP. Keep your existing database file. Then `pip install -r requirements.txt`, restart Uvicorn, and restart Vite. The new tables are created automatically.


## Candidate → HR database sync
Candidate workspace → My Profile → Save profile. HR workspace → Registered Candidates to view stored data. SQLite table `candidate_profiles` is created automatically and profiles are linked to applications by email. Existing database is preserved when replacing only source files.

**Security warning:** Current login is demo-only, endpoints are not authenticated. This version is for fictional demo data only. Never deploy publicly or use real candidate personal data until server-side login, RBAC and privacy controls are implemented.

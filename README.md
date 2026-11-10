# TalentFlow AI

TalentFlow AI is a recruiter-focused talent management prototype for reviewing
candidate profiles, matching documented skills to IT roles, and managing a
lightweight hiring pipeline.

The project includes a Candidate workspace, an HR workspace, a FastAPI backend,
and a seeded SQLite database containing 50 fictional candidate profiles and
applications.

> **Prototype notice:** This application is intended for local demos and
> hackathons. It is not production-ready authentication or recruitment
> software. Use fictional data only.

## Features

### Candidate workspace

- Browse open roles and view job requirements
- Upload a text-based PDF CV for analysis
- Submit and track applications
- Maintain a candidate profile

### HR workspace

- Dashboard with hiring funnel metrics
- All Candidates directory with search and IT specialization filters
- Top Candidates ranked by documented skill coverage
- Candidate profiles, applications, and status updates
- Candidate comparison
- Bulk PDF/DOCX CV upload
- Interview, verification, analytics, and notification views

### Demo data

- 50 fictional Azerbaijani IT candidate profiles
- 50 matching demo applications
- 50 searchable PDF CVs in [`demo_cvs/`](./demo_cvs/)
- 10 IT specializations, including Data Scientist, Backend Developer,
  Frontend Developer, AI Engineer, and Cloud Engineer

Candidate names, contact details, CVs, and application records are synthetic.
The included email addresses use `example.com` and are not real accounts.

## Technology

- **Frontend:** React, Vite, Tailwind CSS, Lucide icons
- **Backend:** Python, FastAPI, Uvicorn
- **Database:** SQLite
- **Document parsing:** PyMuPDF and python-docx
- **Optional analysis:** OpenAI API with a transparent keyword-matching
  fallback when no API key is configured

## Requirements

- Python 3.10 or newer
- Node.js 18 or newer (Node.js 20+ recommended)
- npm

## Run locally

### 1. Start the backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate          # macOS/Linux
# .venv\Scripts\activate           # Windows PowerShell
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

The API and interactive documentation are available at
<http://localhost:8000/docs>.

### 2. Start the frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open <http://localhost:5173> in a browser.

On first startup, an empty database is populated from
[`backend/seed_50_candidates.json`](./backend/seed_50_candidates.json). Existing
candidate records are not overwritten.

## Demo walkthrough

1. Select **HR / Recruiter** and create a demo workspace.
2. Open **HR Intelligence** to review dashboard metrics.
3. Use **All Candidates** to browse all 50 profiles.
4. Use **Top Candidates** and select a specialization to view skill coverage.
5. Open **Candidate Pipeline** to review application statuses.
6. For the candidate flow, switch to **Candidate**, choose a job, upload a
   fictional PDF CV, and submit an application.

## Skill coverage

Candidate ranking is based on keyword evidence found in the candidate profile
and CV text. The interface displays matched and missing role skills so that the
result is explainable.

This score is not an AI hiring prediction, a qualification decision, or an
assessment of personal characteristics. All candidate decisions require human
review.

## Optional OpenAI analysis

To enable optional OpenAI-powered CV analysis, set the key before starting the
backend:

```bash
export OPENAI_API_KEY="your-key"
export OPENAI_MODEL="gpt-4o-mini"  # optional
```

Never commit API keys or other secrets. Without a key, the application uses its
local keyword-matching demo mode.

## Project structure

```text
backend/
  main.py                    FastAPI application
  requirements.txt           Python dependencies
  seed_50_candidates.json    Synthetic candidate seed data
  seed_50_candidates.py      Database seeding utility
  talentflow.db              Seeded local SQLite database
demo_cvs/                    Synthetic PDF CVs
frontend/
  src/main.jsx               React application
  src/index.css              Application styles
  package.json               Frontend scripts and dependencies
```

## Security and production limitations

This prototype intentionally omits production controls:

- The demo role selector is not authentication.
- API routes do not enforce user identity or role-based authorization.
- There is no rate limiting, audit trail, retention policy, or production
  document access control.
- CV parsing is heuristic and does not provide OCR for scanned documents.
- Bulk analysis runs synchronously and is not designed for large workloads.
- Candidate CV text is stored in SQLite.

Do not expose the development server publicly or upload real personal,
employment, medical, or other sensitive information. A production deployment
requires authenticated accounts, RBAC, secure document storage, privacy
controls, background processing, monitoring, and an independent security
review.
## Author

Aysel Musayeva

Zeynab Gurbanova

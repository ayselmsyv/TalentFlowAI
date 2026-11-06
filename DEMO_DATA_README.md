# TalentFlow AI — 50 synthetic Azerbaijani IT candidates

This is **fictional demo data**, not real applicants. All names, roles, experience, email addresses, and documents are fabricated. `example.com` addresses are not real contact accounts.

## Run the complete seeded app
1. Extract the full project ZIP.
2. Backend: `cd backend`; `pip install -r requirements.txt`; `uvicorn main:app --reload`.
3. Frontend: `cd frontend`; `npm install`; `npm run dev`.
4. In the browser select **HR Demo** → **HR Intelligence** → Candidates, Comparison, Analytics, Registered Candidates.

## Import into your existing app (without replacing your data)
The included `backend/talentflow.db` is a **standalone seeded database**. Replacing your own `talentflow.db` will replace your local data, so back up first. To merge safely, use the included `backend/seed_50_candidates.py` script, which imports profiles and applications into your current database and skips existing matching email+job pairs.

## What is included
- 50 one-page searchable PDF CVs in `demo_cvs/`
- 50 `candidate_profiles` records
- 50 job applications linked to 10 IT job categories
- Explanation-based keyword coverage scores (not AI hiring probabilities)
- Demo interview and certificate-verification metadata

## Limitations
This is for local demonstration only. Existing login is not secure authentication and API endpoints are not protected by role permissions. Do not deploy publicly or add real applicant or medical data.

# TalentFlow AI — IT Talent Pool and Top Candidates

This version adds **Top Candidates** directly to the HR sidebar and to the HR Intelligence navigation. All 50 fictional Azerbaijani IT candidate profiles are preloaded in `backend/talentflow.db`.

1. Open the `talentflow-ai` folder in VS Code.
2. Backend terminal: `cd backend`, `pip install -r requirements.txt`, `python -m uvicorn main:app --reload --port 8000`.
3. Frontend terminal: `cd frontend`, `npm install`, `npm run dev -- --port 5173 --strictPort`.
4. In the app select HR Demo, then **Top Candidates**. Select Data Scientist, Cybersecurity Analyst, Data Analyst, Frontend Developer, Backend Developer, AI Engineer, DevOps Engineer, QA Automation Engineer, Cloud Engineer or Mobile Developer.
5. Candidate profiles are ranked by coverage of predefined, role-specific skills present in candidate-entered skills or their CV text. Missing evidence is shown; this is not an AI prediction or employment suitability assessment.

API: `GET http://localhost:8000/api/hr/talent-pool` returns registered profiles with their specialization, CV text, and application IDs. Demo-only access: no production authorization; use fictional data only.

If candidates are missing, ensure the running backend uses the database in this ZIP, not an older project folder.

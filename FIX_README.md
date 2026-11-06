# TalentFlow AI — Candidate Directory Fix

This version includes the 50 fictional candidates in `backend/talentflow.db` and automatically imports them on backend startup **only if both the candidate_profiles and applications tables are empty**. Existing records are not overwritten.

## Windows instructions
1. Stop older frontend/backend terminals (`Ctrl+C`).
2. Extract this ZIP to a new short folder, e.g. `C:\TalentFlowFixed`. Open the **talentflow-ai** subfolder in VS Code.
3. Backend terminal: `cd backend` then `python -m pip install -r requirements.txt` then `python -m uvicorn main:app --reload --port 8000`.
4. Frontend terminal (from project root): `cd frontend` then `npm install` then `npm run dev -- --port 5173 --strictPort`.
5. Open `http://localhost:8000/api/hr/demo-health`. It should report `profiles: 50` and `applications: 50` for the bundled demo database.
6. Open `http://localhost:5173`, select HR Demo, then HR Intelligence → Candidates.

If the API shows 50 applications but the browser is empty, hard-refresh the page (Ctrl+Shift+R). Ensure no old frontend server occupies port 5173.

The login is demo-only. Do not use real candidate data.

# HR Candidate Directory update

- HR Intelligence > All Candidates displays all 50 registered profiles (even without applications).
- Selecting an IT specialization triggers a database-backed API request and returns specialization matches first, then other candidates sorted by documented skill coverage.
- Search filters candidates server-side; applications remain in their own tab.
- Backend endpoint: GET /api/hr/directory?specialization=Data%20Scientist&search=
- Database indexes accelerate candidate-email joins and name sorting.
- CV skill coverage is keyword evidence only, not a hiring prediction.

## Run
Backend: cd backend && python -m uvicorn main:app --reload --port 8000
Frontend: cd frontend && npm install && npm run dev
Open HR Demo > HR Intelligence > All Candidates.

Demo authentication only. Use synthetic candidate data.

"""Idempotent synthetic demo seed. Run from backend: python seed_50_candidates.py"""
import json
from pathlib import Path
import main

def seed_demo():
    records=json.loads((Path(__file__).parent/'seed_50_candidates.json').read_text(encoding='utf-8'))
    with main.db() as con:
        for p in records:
            row=con.execute('SELECT * FROM jobs WHERE title=?',(p['title'],)).fetchone()
            if not row:
                con.execute('INSERT INTO jobs(title,company,description,requirements,education,experience) VALUES (?,?,?,?,?,?)', (p['title'],'Caspian Digital Demo','Synthetic IT vacancy',p['requirements'],'Computer Science or equivalent','Junior to mid-level'))
                row=con.execute('SELECT * FROM jobs WHERE title=?',(p['title'],)).fetchone()
            con.execute("INSERT INTO candidate_profiles(email,full_name,phone,location,education,experience,skills,languages,certifications,projects) VALUES (?,?,?,?,?,?,?,?,?,?) ON CONFLICT(email) DO NOTHING", (p['email'],p['name'],'+994 00 000 00 00',p['location'],p['education'],p['experience'],p['skills'],p['languages'],p['certifications'],p['projects']))
            if not con.execute('SELECT 1 FROM applications WHERE candidate_email=? AND job_id=?',(p['email'],row['id'])).fetchone():
                result=main.local_analysis(p['cv_text'],dict(row))
                con.execute('INSERT INTO applications(job_id,candidate_name,candidate_email,cv_text,status,analysis) VALUES(?,?,?,?,?,?)', (row['id'],p['name'],p['email'],p['cv_text'],'Applied',json.dumps(result,ensure_ascii=False)))
    print('Seed complete: 50 fictional candidates available in HR workspace (existing records preserved).')

if __name__ == '__main__':
    seed_demo()

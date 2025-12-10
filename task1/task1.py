resume_skills = input("Enter your resume skills (comma separated): ").lower().split(",")
job_skills = input("Enter job required skills (comma separated): ").lower().split(",")
resume_skills = [skill.strip() for skill in resume_skills]
job_skills = [skill.strip() for skill in job_skills]
matched = set(resume_skills) & set(job_skills)
missing = set(job_skills) - set(resume_skills)
print("Matched skills:", matched)
print("Missing skills:", missing)


OUTPUT
Enter your resume skills (comma separated): Python, SQL, HTML 
Enter job required skills (comma separated): Python, Java, SQL
Matched skills: {'python', 'sql'}
Missing skills: {'java'}

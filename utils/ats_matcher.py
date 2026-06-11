def calculate_ats_score(
        resume_skills,
        job_description
):

    if not job_description:
        return 0, [], []

    job_description = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in resume_skills:

        if skill.lower() in job_description:
            matched_skills.append(skill)

    common_skills = [
        "python",
        "django",
        "fastapi",
        "flask",
        "aws",
        "docker",
        "kubernetes",
        "sql",
        "postgresql",
        "mysql",
        "mongodb",
        "git",
        "linux",
        "javascript",
        "html",
        "css",
        "react",
        "typescript",
        "machine learning",
        "data science",
        "llm",
        "large language models",
        "object oriented programming",
        "design patterns",
        "software architecture",
        "full stack",
        "automation",
        "dashboard",
        "tableau",
        "qlikview",
        "qliksense"
    ]

    for skill in common_skills:

        if (
            skill in job_description
            and skill not in matched_skills
        ):
            missing_skills.append(skill)

    if len(common_skills) == 0:
        score = 0
    else:
        score = round(
            (
                len(matched_skills)
                /
                len(
                    [
                        s for s in common_skills
                        if s in job_description
                    ]
                )
            ) * 100,
            2
        )

    return score, matched_skills, missing_skills
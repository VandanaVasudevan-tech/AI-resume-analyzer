def calculate_resume_score(
        skills_count,
        experience_years,
        education_found
):

    score = 0

    score += min(
        skills_count * 5,
        40
    )

    try:
        exp = float(
            experience_years
        )

        score += min(
            exp * 5,
            30
        )

    except:
        pass

    if education_found:
        score += 20

    return min(
        score,
        100
    )
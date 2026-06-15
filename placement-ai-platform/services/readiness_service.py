def calculate_readiness_score(student: dict):
    """
    Rule-based readiness scoring.
    Total Score = 100
    """

    score = 0
    reasons = []

    # =====================
    # Academic Score (20)
    # =====================

    cgpa = student.get("cgpa", 0)

    if cgpa >= 9:
        score += 20
        reasons.append("Excellent CGPA")
    elif cgpa >= 8:
        score += 15
        reasons.append("Good CGPA")
    elif cgpa >= 7:
        score += 10
        reasons.append("Average CGPA")
    else:
        score += 5
        reasons.append("Low CGPA")

    # =====================
    # Skills Score (30)
    # =====================

    skills = [s.lower() for s in student.get("skills", [])]

    important_skills = {
        "python": 5,
        "sql": 5,
        "machine learning": 10,
        "deep learning": 5,
        "fastapi": 3,
        "docker": 3,
        "aws": 4,
        "git": 3,
        "mongodb": 2
    }

    skill_score = 0

    for skill, points in important_skills.items():
        if skill in skills:
            skill_score += points

    skill_score = min(skill_score, 30)

    score += skill_score

    reasons.append(
        f"Skill Score = {skill_score}/30"
    )

    # =====================
    # Project Score (20)
    # =====================

    projects = student.get("projects", [])

    if len(projects) >= 3:
        score += 20
        reasons.append("Strong Project Portfolio")
    elif len(projects) >= 2:
        score += 15
        reasons.append("Good Project Experience")
    elif len(projects) >= 1:
        score += 10
        reasons.append("Basic Project Experience")
    else:
        reasons.append("No Projects")

    # =====================
    # Internship Score (15)
    # =====================

    internships = student.get("internships", [])

    if len(internships) > 0:
        score += 15
        reasons.append("Internship Experience Present")
    else:
        reasons.append("No Internship Experience")

    # =====================
    # Certification Score (15)
    # =====================

    certifications = student.get(
        "certifications",
        []
    )

    if len(certifications) >= 3:
        score += 15
        reasons.append("Multiple Certifications")
    elif len(certifications) >= 1:
        score += 10
        reasons.append("Some Certifications")
    else:
        reasons.append("No Certifications")

    # =====================
    # Category
    # =====================

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Ready"
    elif score >= 60:
        category = "Improving"
    else:
        category = "At Risk"

    return {
        "score": score,
        "category": category,
        "reasoning": reasons
    }
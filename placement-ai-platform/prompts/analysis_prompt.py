def build_analysis_prompt(student_data):
    return f"""
You are an expert Placement Readiness Analyst.

Analyze the student profile below.

Student Name:
{student_data.get('name')}

College:
{student_data.get('college')}

Degree:
{student_data.get('degree')}

CGPA:
{student_data.get('cgpa')}

Graduation Year:
{student_data.get('graduation_year')}

Skills:
{student_data.get('skills')}

Projects:
{student_data.get('projects')}

Internships:
{student_data.get('internships')}

Certifications:
{student_data.get('certifications')}

Resume:
{student_data.get('resume_text')}

Provide the response ONLY in JSON format.

JSON Format:

{{
    "summary":"",

    "strengths":[
        ""
    ],

    "improvements":[
        ""
    ],

    "recommended_skills":[
        ""
    ],

    "job_roles":[
        ""
    ],

    "reasoning":""
}}

Do not return markdown.

Return only valid JSON.
"""
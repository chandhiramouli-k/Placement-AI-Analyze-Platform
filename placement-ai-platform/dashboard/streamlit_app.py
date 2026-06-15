import streamlit as st
import requests
import pandas as pd

# =========================
# CONFIG
# =========================
API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Placement AI Platform",
    layout="wide"
)

st.title("🎓 AI Placement Readiness System")

# =========================
# LOAD DATA FUNCTIONS
# =========================
def get_students():
    res = requests.get(f"{API_URL}/students/")
    if res.status_code == 200:
        return res.json().get("students", [])
    return []

def analyze_student(student_id):
    return requests.post(f"{API_URL}/analysis/{student_id}")

# =========================
# SIDEBAR MENU
# =========================
menu = st.sidebar.radio(
    "Navigation",
    [
        "📋 Students",
        "➕ Add Student",
        "🧠 AI Analysis",
        "📊 Analytics"
    ]
)

# =========================
# VIEW STUDENTS
# =========================
if menu == "📋 Students":

    st.subheader("Student Records")

    students = get_students()

    if not students:
        st.warning("No students found")
        st.stop()

    df = pd.DataFrame(students)

    st.dataframe(
        df[["name", "email", "cgpa", "graduation_year"]],
        use_container_width=True
    )

    st.divider()

    selected = st.selectbox(
        "Select Student",
        students,
        format_func=lambda x: x["name"]
    )

    st.write("### Full Profile")
    st.json(selected)

    if selected.get("ai_analysis"):
        st.write("### AI Insights")
        st.json(selected["ai_analysis"])

# =========================
# ADD STUDENT
# =========================
elif menu == "➕ Add Student":

    st.subheader("Create Student Profile")

    with st.form("student_form"):

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)

        with col2:
            college = st.text_input("College")
            degree = st.text_input("Degree")
            graduation_year = st.number_input("Graduation Year", 2020, 2035, 2026)

        skills = st.text_area("Skills (comma separated)")
        projects = st.text_area("Projects (comma separated)")
        certifications = st.text_area("Certifications (comma separated)")
        internships = st.text_area("Internships (comma separated)")

        submit = st.form_submit_button("Create Student")

        if submit:

            payload = {
                "name": name,
                "email": email,
                "phone": phone,
                "college": college,
                "degree": degree,
                "cgpa": cgpa,
                "graduation_year": graduation_year,
                "skills": [s.strip() for s in skills.split(",") if s.strip()],
                "projects": [
                    {"title": p.strip(), "description": ""}
                    for p in projects.split(",") if p.strip()
                ],
                "certifications": [c.strip() for c in certifications.split(",") if c.strip()],
                "internships": [i.strip() for i in internships.split(",") if i.strip()],
                "resume_text": ""
            }

            res = requests.post(
                f"{API_URL}/students/",
                json=payload
            )

            if res.status_code == 200:
                st.success("Student created successfully")
                st.json(res.json())
            else:
                st.error("Failed to create student")

# =========================
# AI ANALYSIS
# =========================
elif menu == "🧠 AI Analysis":

    st.subheader("AI Placement Analysis")

    students = get_students()

    if not students:
        st.warning("No students available")
        st.stop()

    selected = st.selectbox(
        "Select Student",
        students,
        format_func=lambda x: x["name"]
    )

    if st.button("Run AI Analysis"):

        with st.spinner("Analyzing profile using AI..."):

            res = analyze_student(selected["_id"])

            if res.status_code == 200:

                data = res.json()["analysis"]

                st.success("Analysis Completed")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Readiness Score", data.get("readiness_score"))
                    st.write("### Strengths")
                    st.write(data.get("strengths"))

                    st.write("### Recommended Skills")
                    st.write(data.get("recommended_skills"))

                with col2:
                    st.write("### Improvements")
                    st.write(data.get("improvements"))

                    st.write("### Job Roles")
                    st.write(data.get("job_roles"))

                st.write("### Summary")
                st.info(data.get("summary"))

                st.write("### Reasoning")
                st.write(data.get("reasoning"))

            else:
                st.error("AI analysis failed")

# =========================
# ANALYTICS DASHBOARD
# =========================
elif menu == "📊 Analytics":

    st.subheader("Placement Analytics Overview")

    students = get_students()

    if not students:
        st.warning("No data available")
        st.stop()

    df = pd.DataFrame(students)

    st.metric("Total Students", len(df))

    # Readiness scores
    scores = [
        s.get("ai_analysis", {}).get("readiness_score", 0)
        for s in students
    ]

    if scores:
        st.metric("Average Readiness Score", round(sum(scores) / len(scores), 2))

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("CGPA Distribution")
        st.bar_chart(df["cgpa"])

    with col2:
        st.subheader("Graduation Year Distribution")
        st.bar_chart(df["graduation_year"])
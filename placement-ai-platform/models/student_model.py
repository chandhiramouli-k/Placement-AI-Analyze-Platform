from pydantic import BaseModel
from typing import List, Optional


class Project(BaseModel):
    title: str
    description: str


class AIAnalysis(BaseModel):
    summary: Optional[str] = ""
    strengths: Optional[List[str]] = []
    improvements: Optional[List[str]] = []
    recommended_skills: Optional[List[str]] = []
    job_roles: Optional[List[str]] = []
    readiness_score: Optional[int] = 0
    reasoning: Optional[str] = ""


class Student(BaseModel):
    name: str
    email: str
    phone: str

    college: str
    degree: str

    cgpa: float
    graduation_year: int

    skills: List[str] = []

    projects: List[Project] = []

    certifications: List[str] = []

    internships: List[str] = []

    resume_text: Optional[str] = ""

    ai_analysis: Optional[AIAnalysis] = AIAnalysis()
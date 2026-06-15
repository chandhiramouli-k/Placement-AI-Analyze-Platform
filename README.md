# 🎓 Placement Readiness AI Platform

An AI-powered web application that helps students prepare for campus placements by analyzing their academic profile, skills, and experience to generate **readiness scores, strengths, skill gaps, and job role recommendations**.

---

# 🚀 Features

## 👨‍🎓 Student Management
- Add student profiles
- View all students
- Update student data
- Delete student records

## 🧠 AI-Powered Analysis
- Student profile summary
- Strength identification
- Weakness & improvement areas
- Recommended skills
- Suggested job roles
- Placement readiness score (0–100)

## 📊 Dashboard (Streamlit UI)
- Student list view
- Add student form
- AI analysis panel
- Analytics dashboard with charts

## 💾 Database
- MongoDB integration
- Persistent student storage
- AI analysis saved per student

---

# 🏗️ Tech Stack

- ⚡ Backend: FastAPI (Python)
- 🎨 Frontend: Streamlit
- 🧠 AI Model: Ollama (Llama 3.1)
- 🗄️ Database: MongoDB
- 🐍 Language: Python

---

# 📁 Project Structure
placement-ai-platform/
│
├── api/
│ ├── student_routes.py
│ └── analysis_routes.py
│
├── database/
│ └── mongodb.py
│
├── models/
│ └── student_model.py
│
├── services/
│ ├── student_service.py
│ ├── ai_service.py
│ └── readiness_service.py
│
├── prompts/
│ └── analysis_prompt.py
│
├── utils/
│ └── helpers.py
│
├── dashboard/
│ └── streamlit_app.py
│
├── main.py
├── requirements.txt
└── .env


---

# ⚙️ Installation

## 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/placement-ai-platform.git
cd placement-ai-platform
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Start MongoDB
mongod
5️⃣ Start Ollama AI

Install from:
https://ollama.ai

Then run:

ollama serve
ollama pull llama3.1
6️⃣ Configure Environment Variables

Create .env file:

MONGO_URI=mongodb://localhost:27017
DB_NAME=placement_ai_db

OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=llama3.1
🚀 Run the Project
1️⃣ Start Backend (FastAPI)
uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs

2️⃣ Start Frontend (Streamlit)
streamlit run dashboard/streamlit_app.py

Open:
http://localhost:8501



👨‍💻 Author

Chandhiramouli K
Final Year CSE (AI & ML) Student
Passionate about AI, ML, and Full Stack Development

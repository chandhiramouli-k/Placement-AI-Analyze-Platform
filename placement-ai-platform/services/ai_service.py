import os
import json
import requests

from dotenv import load_dotenv

from prompts.analysis_prompt import (
    build_analysis_prompt
)

load_dotenv()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.1"
)


def analyze_student(student_data):
    """
    Send student profile to Ollama.
    """

    prompt = build_analysis_prompt(
        student_data
    )

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        llm_output = result.get(
            "response",
            ""
        )

        try:
            parsed_output = json.loads(
                llm_output
            )

            return parsed_output

        except Exception:

            return {
                "summary":
                    "AI response parsing failed.",

                "strengths": [],

                "improvements": [],

                "recommended_skills": [],

                "job_roles": [],

                "reasoning": llm_output
            }

    except Exception as e:

        return {
            "summary":
                "AI analysis failed.",

            "strengths": [],

            "improvements": [],

            "recommended_skills": [],

            "job_roles": [],

            "reasoning": str(e)
        }
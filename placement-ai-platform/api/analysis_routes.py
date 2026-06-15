from fastapi import (
    APIRouter,
    HTTPException
)

from bson import ObjectId

from database.mongodb import (
    students_collection
)

from utils.helpers import (
    is_valid_object_id
)

from services.ai_service import (
    analyze_student
)

from services.readiness_service import (
    calculate_readiness_score
)

router = APIRouter()


@router.post("/{student_id}")
def analyze_student_profile(
    student_id: str
):

    # =====================
    # Validate ID
    # =====================

    if not is_valid_object_id(
        student_id
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid Student ID"
        )

    # =====================
    # Get Student
    # =====================

    student = students_collection.find_one(
        {
            "_id":
            ObjectId(student_id)
        }
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # =====================
    # Convert ObjectId
    # =====================

    student["_id"] = str(
        student["_id"]
    )

    # =====================
    # Rule Based Score
    # =====================

    readiness_result = (
        calculate_readiness_score(
            student
        )
    )

    # =====================
    # AI Analysis
    # =====================

    ai_result = analyze_student(
        student
    )

    # =====================
    # Merge Results
    # =====================

    final_analysis = {

        "summary":
            ai_result.get(
                "summary",
                ""
            ),

        "strengths":
            ai_result.get(
                "strengths",
                []
            ),

        "improvements":
            ai_result.get(
                "improvements",
                []
            ),

        "recommended_skills":
            ai_result.get(
                "recommended_skills",
                []
            ),

        "job_roles":
            ai_result.get(
                "job_roles",
                []
            ),

        "readiness_score":
            readiness_result["score"],

        "readiness_category":
            readiness_result["category"],

        "reasoning":
            ai_result.get(
                "reasoning",
                ""
            ),

        "score_breakdown":
            readiness_result[
                "reasoning"
            ]
    }

    # =====================
    # Save In MongoDB
    # =====================

    students_collection.update_one(
        {
            "_id":
            ObjectId(student_id)
        },
        {
            "$set":
            {
                "ai_analysis":
                final_analysis
            }
        }
    )

    return {
        "message":
            "Analysis completed",

        "student_id":
            student_id,

        "analysis":
            final_analysis
    }
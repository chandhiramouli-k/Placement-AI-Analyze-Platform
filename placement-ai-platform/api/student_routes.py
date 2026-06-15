from fastapi import (
    APIRouter,
    HTTPException
)

from models.student_model import Student

from services.student_service import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)

router = APIRouter()


# ==========================
# CREATE STUDENT
# ==========================

@router.post("/")
def create_student_api(
    student: Student
):

    created_student = create_student(
        student.model_dump()
    )

    return {
        "message":
            "Student created successfully",

        "student":
            created_student
    }


# ==========================
# GET ALL STUDENTS
# ==========================

@router.get("/")
def get_students_api():

    students = get_all_students()

    return {
        "count": len(students),
        "students": students
    }


# ==========================
# GET STUDENT BY ID
# ==========================

@router.get("/{student_id}")
def get_student_api(
    student_id: str
):

    student = get_student_by_id(
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# ==========================
# UPDATE STUDENT
# ==========================

@router.put("/{student_id}")
def update_student_api(
    student_id: str,
    student: Student
):

    updated_student = update_student(
        student_id,
        student.model_dump()
    )

    if not updated_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message":
            "Student updated successfully",

        "student":
            updated_student
    }


# ==========================
# DELETE STUDENT
# ==========================

@router.delete("/{student_id}")
def delete_student_api(
    student_id: str
):

    success = delete_student(
        student_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message":
            "Student deleted successfully"
    }
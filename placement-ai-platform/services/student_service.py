from bson import ObjectId

from database.mongodb import (
    students_collection
)


def serialize_student(student):

    student["_id"] = str(student["_id"])

    return student


# ==========================
# CREATE
# ==========================

def create_student(student_data):

    result = students_collection.insert_one(
        student_data
    )

    created_student = students_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_student(
        created_student
    )


# ==========================
# GET ALL
# ==========================

def get_all_students():

    students = students_collection.find()

    return [
        serialize_student(student)
        for student in students
    ]


# ==========================
# GET BY ID
# ==========================

def get_student_by_id(student_id):

    student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if not student:
        return None

    return serialize_student(student)


# ==========================
# UPDATE
# ==========================

def update_student(
    student_id,
    update_data
):

    result = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {
            "$set": update_data
        }
    )

    if result.modified_count == 0:

        student = students_collection.find_one(
            {"_id": ObjectId(student_id)}
        )

        if not student:
            return None

    updated_student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    return serialize_student(
        updated_student
    )


# ==========================
# DELETE
# ==========================

def delete_student(student_id):

    result = students_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    return result.deleted_count > 0
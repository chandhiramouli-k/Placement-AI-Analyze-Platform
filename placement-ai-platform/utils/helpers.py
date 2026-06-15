from bson import ObjectId


def is_valid_object_id(id_value: str):

    try:
        ObjectId(id_value)
        return True

    except Exception:
        return False
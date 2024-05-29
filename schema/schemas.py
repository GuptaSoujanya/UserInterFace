def individual_serializer(user_data) -> dict:
    return {
        "id": str(user_data.get("_id", "")),
        "name": user_data.get("name", ""),
        "password": user_data.get("password", ""),
        "email": user_data.get("email", "")
    }

def list_serial(user_datas) -> list:
    return [individual_serializer(user_data) for user_data in user_datas]
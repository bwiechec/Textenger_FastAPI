def individual_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "lastChangeTimestamp": user["lastChangeTimestamp"]
    }

def list_serial(users) -> list:
    return [individual_serial(user) for user in users]
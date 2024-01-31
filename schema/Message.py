def individual_serial(message) -> dict:
    return {
        "id": str(message["_id"]),
        "threadId": message["threadId"],
        "userId": message["userId"],
        "message": message["message"],
        "timestamp": message["timestamp"],
        "withoutBg": message["withoutBg"]
    }

def list_serial(messages) -> list:
    return [individual_serial(message) for message in messages]
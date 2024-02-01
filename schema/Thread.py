def individual_serial(thread) -> dict:
    return {
        "id": str(thread["_id"]),
        "name": thread["name"],
        "emoji": thread["emoji"],
        "color_sent": thread["color_sent"],
        "color_received": thread["color_received"],
        "participants": thread["participants"]
    }

def list_serial(threads) -> list:
    return [individual_serial(thread) for thread in threads]
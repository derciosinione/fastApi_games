def gameEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "description": str(item["description"]),
        "imageUrl": str(item["imageUrl"]),
        "isActive": bool(item["imageUrl"]),
    }
    

def gamesEntities(entities) -> list:
    return [gameEntity(item) for item in entities]
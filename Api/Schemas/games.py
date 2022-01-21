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

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeList(a) for a in entity]

def serializeDict(entity) -> dict:
    return {**{i:str(entity[i]) for i in entity if i=='_id'},**{i:entity[i] for i in entity if i!='_id'}}

def serializeList(entities) -> list:
    return [serializeList(entity) for entity in entities]
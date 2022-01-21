from bson import ObjectId

from Api.Config.db import db
from Api.Models.Dto.CreateGameDto import CreateGame
from Api.Schemas.serializeObjects import serializeDict, serializeList


async def getAll():
    return serializeList(db.games.find())


async def getById(id):
    return serializeDict(db.games.find_one({"_id": ObjectId(id)}))    


async def createGame(game: CreateGame):
    result = db.games.insert_one(dict(game))
    return serializeDict(db.games.find_one({"_id": ObjectId(result.inserted_id)}))


async def updateGame(id, game: CreateGame):
    db.games.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(game)})
    return serializeDict(db.games.find_one({"_id": ObjectId(id)}))


async def deleteGame(id) -> bool:
    db.games.find_one_and_delete({"_id": ObjectId(id)})
    return True

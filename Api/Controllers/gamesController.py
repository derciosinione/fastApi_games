from fastapi import APIRouter, status, Response
from bson import ObjectId

from Api.Config.db import db
from Api.Models.Dto.CreateGameDto import CreateGame
from Api.Schemas.games import gamesEntities, gameEntity
from Api.Models.games import Games


games = APIRouter()

@games.get('/games', status_code=status.HTTP_200_OK)
async def getAll():
    return gamesEntities(db.games.find())

@games.get('/games/{id}')
async def getById(id, response: Response):
    result = db.games.find_one({"_id": ObjectId(id)})
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"Could not find game with the given Id"}
    return gameEntity(result)
    

@games.post('/games', status_code=status.HTTP_200_OK)
async def createGame(game: CreateGame):
    result = db.games.insert_one(dict(game))
    inserted = db.games.find_one({"_id": ObjectId(result.inserted_id)})
    return gameEntity(inserted)


@games.put('/games/{id}', status_code=status.HTTP_200_OK)
async def updateGame(id, game: CreateGame, response: Response):
    game = db.games.find_one({"_id": ObjectId(id)})
    if game is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"Could not find game with the given Id"}
    
    db.games.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(game)})
    return gameEntity(db.games.find_one({"_id": ObjectId(id)}))


@games.delete('/games/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteGame(id, response: Response):
    game = db.games.find_one({"_id": ObjectId(id)})
    if game is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"Could not find game with the given Id"}
    
    db.games.find_one_and_delete({"_id": ObjectId(id)})
    return None

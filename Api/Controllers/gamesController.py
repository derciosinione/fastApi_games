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

@games.post('/games', status_code=status.HTTP_200_OK)
async def createGame(game: CreateGame):
    result = db.games.insert_one(dict(game))
    inserted = db.games.find_one({"_id": ObjectId(result.inserted_id)})
    return gameEntity(inserted)

@games.put('/games/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def updateGame(id, game: CreateGame, response: Response):
    # db.games.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(game)})
    response.status_code = status.HTTP_404_NOT_FOUND
    return None
from fastapi import status, Response, File, UploadFile, HTTPException
from bson import ObjectId

from Api.Config.db import db
from Api.Models.Dto.CreateGameDto import CreateGame
from Api.Schemas.serializeObjects import serializeDict, serializeList
from Api.helpers.save_picture import save_picture
from Api.Routes import gamesRoutes


_notFoundMessage = "Could not find game with the given Id"


@gamesRoutes.get('/games', status_code=status.HTTP_200_OK)
async def getAll():
    return serializeList(db.games.find())


@gamesRoutes.get('/games/{id}')
async def getById(id):
    result = db.games.find_one({"_id": ObjectId(id)})
    await riseHttpExceptionIfNotFound(result)
    return serializeDict(result)    


@gamesRoutes.post('/games', status_code=status.HTTP_200_OK)
async def createGame(game: CreateGame):
    result = db.games.insert_one(dict(game))
    inserted = db.games.find_one({"_id": ObjectId(result.inserted_id)})
    return serializeDict(inserted)


@gamesRoutes.put('/games/{id}', status_code=status.HTTP_200_OK)
async def updateGame(id, game: CreateGame):
    result = db.games.find_one({"_id": ObjectId(id)})
    await riseHttpExceptionIfNotFound(result)
    db.games.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(game)})
    return serializeDict(db.games.find_one({"_id": ObjectId(id)}))


@gamesRoutes.delete('/games/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteGame(id, response: Response):
    result = db.games.find_one({"_id": ObjectId(id)})
    await riseHttpExceptionIfNotFound(result)
    db.games.find_one_and_delete({"_id": ObjectId(id)})
    return None


@gamesRoutes.post('/games/{id}/image-upload', status_code=status.HTTP_200_OK)
async def uploadGameImage(id: str, file: UploadFile = File(...)):
    result = db.games.find_one({"_id": ObjectId(id)})
    await riseHttpExceptionIfNotFound(result)
    filename = save_picture(file=file, folderName='games', fileName=result['name'])
    db.games.find_one_and_update({"_id": ObjectId(id)}, {"$set": { "imageUrl": filename }})
    return serializeDict(db.games.find_one({"_id": ObjectId(id)}))


async def riseHttpExceptionIfNotFound(result):
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=_notFoundMessage)


# @gamesRoutes.post('/games/create-file', status_code=status.HTTP_200_OK)
# async def uploadGameImage(file: bytes = File(...)):
#     return { "size": len(file)}


from fastapi import status, File, UploadFile, HTTPException
from bson import ObjectId

from Api.Config.db import db
from Api.Models.Dto.CreateGameDto import CreateGame
from Api.Schemas.serializeObjects import serializeDict, serializeList
from Api.helpers.save_picture import save_picture
from Api.Routes import gamesRoutes
from Api.Services import gamesService as service


_notFoundMessage = "Could not find game with the given Id"


@gamesRoutes.get('/games', status_code=status.HTTP_200_OK)
async def getAll():
    return await service.getAll()


@gamesRoutes.get('/games/{id}')
async def getById(id):
    result = await service.getById(id)
    await riseHttpExceptionIfNotFound(result)
    return result   
  

@gamesRoutes.post('/games', status_code=status.HTTP_200_OK)
async def InsertGame(game: CreateGame):
    return await service.InsertGame(game)


@gamesRoutes.put('/games/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def updateGame(id, game: CreateGame):
    result = await service.getById(id)
    await riseHttpExceptionIfNotFound(result)
    isUpdated : bool = await service.updateGame(id, game);
    if not isUpdated:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ocorreu um erro ao editar as informações do jogo")


@gamesRoutes.delete('/games/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteGame(id):
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


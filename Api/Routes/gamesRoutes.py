from bson import objectid
from fastapi import status, File, UploadFile, HTTPException

from Api.Models.Dto.CreateGameDto import CreateGame
from Api.Routes.utils import getResponse, riseHttpExceptionIfNotFound
from Api.helpers.save_picture import save_picture
from Api.Routes import gamesRoutes
from Api.Services import gamesService as service


_notFoundMessage = "Could not find game with the given Id."


@gamesRoutes.get('/games', status_code=status.HTTP_200_OK)
async def getAll():
    return await service.getAll()


@gamesRoutes.get('/games/{id}')
async def getById(id):
    return await resultVerification(id)   
  

@gamesRoutes.post('/games', status_code=status.HTTP_200_OK)
async def InsertGame(game: CreateGame):
    return await service.InsertGame(game)


@gamesRoutes.put('/games/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def updateGame(id, game: CreateGame):
    await resultVerification(id)
    done : bool = await service.updateGame(id, game);
    return getResponse(done, errorMessage="Ocorreu um erro ao editar as informações do jogo.")


@gamesRoutes.delete('/games/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteGame(id):
    await resultVerification(id)
    done : bool = await service.deleteGame(id);
    return getResponse(done, errorMessage="Ocorreu um erro ao eliminar este jogo.")   


@gamesRoutes.post('/games/{id}/image-upload', status_code=status.HTTP_204_NO_CONTENT)
async def uploadGameImage(id: str, file: UploadFile = File(...)):
    await resultVerification(id)
    imageUrl = save_picture(file=file, folderName='games', fileName=result['name'])
    done = await service.savePicture(id, imageUrl)
    return getResponse(done, errorMessage="Ocorreu um erro ao salvar imagem do jogo.")


# Helpers

async def resultVerification(id: objectid) -> dict:
    result = await service.getById(id)
    await riseHttpExceptionIfNotFound(result, message=_notFoundMessage)
    return result

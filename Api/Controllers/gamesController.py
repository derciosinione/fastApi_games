import os, shutil
# import shutil
from uuid import uuid4
from typing import Any
from fastapi import APIRouter, status, Response, File, UploadFile
from bson import ObjectId
from PIL import Image
import PIL
from starlette.routing import request_response 

from Api.Config.db import db
from Api.Models.Dto.CreateGameDto import CreateGame
from Api.Schemas.games import gamesEntities, gameEntity


gamesRoutes = APIRouter()

@gamesRoutes.get('/games', status_code=status.HTTP_200_OK)
async def getAll():
    return gamesEntities(db.games.find())

@gamesRoutes.get('/games/{id}')
async def getById(id, response: Response):
    result = db.games.find_one({"_id": ObjectId(id)})
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"Could not find game with the given Id"}
    return gameEntity(result)
    

@gamesRoutes.post('/games', status_code=status.HTTP_200_OK)
async def createGame(game: CreateGame):
    result = db.games.insert_one(dict(game))
    inserted = db.games.find_one({"_id": ObjectId(result.inserted_id)})
    return gameEntity(inserted)


@gamesRoutes.put('/games/{id}', status_code=status.HTTP_200_OK)
async def updateGame(id, game: CreateGame, response: Response):
    
    result = db.games.find_one({"_id": ObjectId(id)})
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"Could not find game with the given Id"}
    
    db.games.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(game)})
    return gameEntity(db.games.find_one({"_id": ObjectId(id)}))


@gamesRoutes.delete('/games/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteGame(id, response: Response):
    result = db.games.find_one({"_id": ObjectId(id)})
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"Could not find game with the given Id"}
    
    db.games.find_one_and_delete({"_id": ObjectId(id)})
    return None

@gamesRoutes.post('/games/image-upload', status_code=status.HTTP_200_OK)
async def uploadGameImage(file: UploadFile = File(...)):
    save_picture(file)
    # file.filenam
    # with open('test1.jpg', 'wb') as buffer:
    #     shutil.copyfileobj(file.file, buffer)
    #     buffer.close()
    return {"filename": file.filename, "contentType": file.content_type}


@gamesRoutes.post('/games/create-file', status_code=status.HTTP_200_OK)
async def uploadGameImage(file: bytes = File(...)):
    return { "size": len(file)}


def save_picture(picture):
    randon_uid = str(uuid4())
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = randon_uid + f_ext
    picture_path = os.path.join(picture_fn)

    output_size = (125,125)
    img = Image.open(picture.file)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_fn
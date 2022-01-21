from fastapi import APIRouter

defaultRoute = APIRouter()

class GamesRoute:
    route = APIRouter()
    base = '/games/'
    UploadImage = f'{base}image-upload/'



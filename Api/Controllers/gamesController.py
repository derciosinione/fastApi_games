from fastapi import APIRouter

from models.games import Games
from config.db import conn

user = APIRouter()

@user.get('')
async def getAll():
    return conn.local.games.find()
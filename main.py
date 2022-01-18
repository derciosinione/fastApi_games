from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Games(BaseModel):
    id: int
    name: str
    description: str
    image: str
    isActive: Optional[bool] = False


@app.get('/')
async def root():
    return {'message': 'Hello FastApi'}


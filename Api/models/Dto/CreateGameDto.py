from pydantic import BaseModel
from typing import Optional

class CreateGame(BaseModel):
    name: str
    description: str
    imageUrl: str
    isActive: Optional[bool] = False
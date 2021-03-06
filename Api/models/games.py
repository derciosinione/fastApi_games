from pydantic import BaseModel
from typing import Optional

class Games(BaseModel):
    id: int
    name: str
    description: str
    imageUrl: str
    isActive: Optional[bool] = False
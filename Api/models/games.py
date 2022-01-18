from pydantic import BaseModel
from typing import Optional

class Games(BaseModel):
    id: int
    name: str
    description: str
    image: str
    isActive: Optional[bool] = False
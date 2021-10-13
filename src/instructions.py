from pydantic import BaseModel
from element import Element
from typing import List

class Instructions(BaseModel):
    project_id: str
    website: str
    commands: List[Element]
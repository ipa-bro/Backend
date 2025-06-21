from pydantic import BaseModel
from datetime import date 

class SEvents(BaseModel):
     id: int
     photoUrl: str
     title: str
     description: str 
     fullDescription: str
     date: date 
     location: str 

     class Config:
        from_attributes = True


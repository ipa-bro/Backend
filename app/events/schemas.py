from pydantic import BaseModel


class SEvents(BaseModel):
     photoUrl: str
     title: str
     description: str 
     fullDescription: str

     class Config:
        from_attributes = True


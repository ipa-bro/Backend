from pydantic import BaseModel


class SEvents(BaseModel):
     id: int
     photo: str
     title: str
     small_text: str 


     class Config:
        from_attributes = True


class SEvent(BaseModel):
     photo: str
     title: str
     big_text: str 


     class Config:
        from_attributes = True
from datetime import date
from pydantic import BaseModel


class SMembers(BaseModel):
     photo: str
     fullname: str
     position: str
     date_of_birthday: str #date


     class Config:
        from_attributes = True



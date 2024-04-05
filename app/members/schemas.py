from datetime import date
from pydantic import BaseModel


class SMembers(BaseModel):
     photo: str
     fullname: str
     type: str
     date_of_birthday: str #date
     text: str

     class Config:
        from_attributes = True



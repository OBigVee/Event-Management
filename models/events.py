from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    desc: str
    tags: List[str] = Field(sa_column=Column(JSON))
    loc: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example" :{
                "title":"FastAPI BOOK LAUNCH",
                "image":"https://linktomyimage.com/image.png",
                "desc":"discuss about the books contents",
                "tags":["python", "fastapi","book","launch"],
                "loc": "Google Meet"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str]
    image:Optional[str]
    desc:Optional[str]
    tags:Optional[str]
    loc: Optional[str]

    class Config:
        schema_extra ={
            "example":{
                "title":"FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "desc": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book","launch"],
                "loc": "Google Meet"
            }
        }

from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id:int
    title:str
    image: str
    desc: str
    tags: List[str]
    loc: str

    class Config:
        schema_extra = {
            "example":{
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "desc": """We will be discussing 
                    the contents of the FastAPI book in
                        this event. Ensure to come with your
                            own copy to win gifts!""",
                "tags": ["python", "fastapi", "book","launch"],
                "loc": "Google Meet"
            }
        }
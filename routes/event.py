from fastapi import APIRouter, Depends, HTTPException, status
from database.connection import get_session
from sqlmodel import select

from models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(
    tags = ["Events"]
)
events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session))-> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session))-> Event:
    event = session.get(Event, id)
    if event.id == id:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with id {} does not exit".format(id)
    )

@event_router.post("/new")
async def create_event(new_event:Event, session=Depends(get_session)) -> dict:
    """
        The Depends class is responsible for exercising dependency injection in
FastAPI applications. The Depends class takes a truth source such as
a function as an argument and is passed as a function argument in a route,
mandating that the dependency condition be satisfied before any operation can
be executed
    """
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return{
        "message":"Event created successfully"
    }


@event_router.delete("/{id}")
async def delete_event(id: int, session=Depends(get_session))->dict:
    event = session.get(Event, id)
    if event:
            session.delete(event)
            session.commit()
            return{
                "message":"Event remove/Deleted Successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with ID does not exist"
    )


@event_router.delete("/")
async def delete_all_events()-> dict:
    events.clear()
    return{
        "message":"Events deleted successfully"
    }

@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session))-> Event:
    event = session.get(Event, id)
    if event: # if event exists
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Event with id: {} does not exit".format(id) 
    )

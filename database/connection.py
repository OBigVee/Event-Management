from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

database_file = "event_management.db"

db_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(db_connection_string, echo=True, connect_args=connect_args)


def conn():
    """
        create DB as well as table present in `database_file`
    """
    SQLModel.metadata.create_all(engine_url)

def get_session():
    """persists the session in the application"""
    with Session(engine_url) as session:
        yield session
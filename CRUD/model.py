from pydantic import BaseModel

class ShowTodo(BaseModel):
    id: int
    title: str
    status: str
    lastUpdate: str

class InputTodo(BaseModel):
    title: str
    status: str

class User(BaseModel):
    id: int
    username: str
    hashed_password: str
    is_active: bool
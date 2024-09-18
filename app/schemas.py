from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: int
    email: str


class UserLogin(BaseModel):
    email: str
    password: str

class TaskCreate(BaseModel):
    title: str
    description: str
    is_completed: bool = False

class Task(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

    class Config:
        from_attributes = True

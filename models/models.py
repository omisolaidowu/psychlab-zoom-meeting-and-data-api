from fastapi import Form
from dataclasses import dataclass
from bson import ObjectId

from pydantic import BaseModel

@dataclass
class MeetingDetail():
    start_date: str = Form(...)
    start_time: str = Form(...)
    topic: str = Form(...)
    duration: str = Form(...)
    therapist_name: str = Form(...)
    therapist_email: str = Form(...)
    client_name: str = Form(...)
    client_email: str = Form(...)
    

@dataclass
class MeetCode():
    code: str = Form(...)


@dataclass
class MeetingSchedules():
    user_id = ObjectId()
    first_name:str = Form(...)
    last_name:str = Form(...)
    email:str = Form(...)
    days:str = Form(...) 
    scheduleTimes:list = Form(...)
    time: str = Form(None)

@dataclass
class User():
    user_id = ObjectId()
    first_name:str = Form(...)
    last_name:str = Form(...)
    email:str = Form(...)
    Password:str = Form(...)
    isAdmin: bool = Form(False)
    isSuperAdmin: bool = Form(False)
    is_verified: bool = Form(False)

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    message: str
    first_name: str
    status: str

@dataclass
class LoginUserSchema():
    email: str = Form(...)
    password: str = Form(...)

@dataclass
class TokenDelete():
    token: str = Form(...)

@dataclass
class AdminUpdate():
    is_admin: str = Form(...)
    email: str = Form(...)







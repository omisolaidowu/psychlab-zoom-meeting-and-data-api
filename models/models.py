from fastapi import Form

from dataclasses import dataclass

from bson import ObjectId

from pydantic import BaseModel

from typing import Optional

@dataclass
class MeetingDetail():
    start_date: str = Form(...)
    start_time: str = Form(...)

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

@dataclass
class TokenData():
    username: str = Form(...)
    
@dataclass
class Token():
    access_token: str = Form(...)
    token_type: str = Form(...)

@dataclass
class LoginUserSchema():
    email: str = Form(...)
    password: str = Form(...)





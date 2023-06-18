from fastapi import Form

from dataclasses import dataclass

from bson import ObjectId

@dataclass
class MeetingDetail():
    start_date: str = Form(...)
    start_time: str = Form(...)
    

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
    
@dataclass
class Token():
    access_token: str = Form(...)
    token_type: str = Form(...)

@dataclass
class LoginUserSchema():
    email: str = Form(...)
    password: str = Form(...)





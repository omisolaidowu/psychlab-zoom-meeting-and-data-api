from fastapi import Form
from dataclasses import dataclass
from bson import ObjectId

from pydantic import BaseModel
from typing import Optional
# from pydantic import Required
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
    # state: str = Form(MeetingStatus().status)
    # updated_at: str = Form(...)
    # meeting_summary: str = 'null'
    

@dataclass
class MeetCode():
    code: str = Form(...)


@dataclass
class MeetingSchedules():
    user_id = ObjectId()
    first_name:str = Form(...)
    last_name:str = Form(...)
    email:str = Form(...)
    bio: str = Form(...)
    certification: str = Form(...)
    experience: str = Form(...)
    image_path: str = Form(...)
    days:str = Form(None) 
    scheduleTimes:list = Form(None)
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
    email: Optional[str]
    sessions: Optional[list]

@dataclass
class LoginUserSchema():
    email: str = Form(...)
    password: str = Form(...)

@dataclass
class TokenDelete():
    token: str = Form(...)

@dataclass
class GetAllAppointment():
    email: str = Form(...)

@dataclass
class AdminUpdate():
    is_admin: str = Form(...)
    email: str = Form(...)

@dataclass
class TherapistDays():
    email: str = Form(...)
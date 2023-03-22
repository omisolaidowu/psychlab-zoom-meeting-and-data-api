from fastapi import Form

from dataclasses import dataclass

from bson import ObjectId



@dataclass
class MeetingDetail():
    start_time: str = Form(...)

@dataclass
class MeetingSchedules():
    user_id = ObjectId()
    email:str = Form(...)
    name:str = Form(...)
    days:str = Form(...) 
    scheduleTimes:list = Form(...)

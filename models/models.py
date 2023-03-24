from fastapi import Form

from dataclasses import dataclass

from bson import ObjectId



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

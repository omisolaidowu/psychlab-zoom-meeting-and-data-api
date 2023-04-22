import jwt
import requests
import json
from time import time
import sys
import os

from dotenv import load_dotenv
load_dotenv()
sys.path.append(sys.path[0] + "/..")

from errors.errorhandler import Errors
from models.models import MeetingDetail
from services.details import Details


class CreateMeetingInfo(Details, Errors):
    def __init__(self) -> None:
        self.API_key = os.getenv("ZOOM_API-KEY")
        self.API_secret = os.getenv("ZOOM_API_SECRET")
        self.meetingdetails = None
        self.meetingURL: str
        self.meetingPassword: str
        self.meetingTime: str
        self.topic: str

    def generateToken(self):
        token = jwt.encode(
            {'iss': self.API_key, 'exp': time() + 5000},
            self.API_secret,
            algorithm='HS256'
        )
        return token
    # 2023-03-24: 21:57
    
    
    def createMeeting(self, meetings: MeetingDetail):
        try:
            headers = {
                    'authorization': 'Bearer ' + self.generateToken(),
                    'content-type': 'application/json'
                    }
            r = requests.post(
                f'https://api.zoom.us/v2/users/me/meetings',
                headers=headers, data=json.dumps(self.meetDetails(
                "{}T10: {}".format(meetings.start_date, meetings.start_time)
                )))
            meetingdata = json.loads(r.text)
           
            self.meetingURL = meetingdata["join_url"]
            self.meetingPassword = meetingdata["password"]
            self.meetingTime = meetingdata["start_time"]
            self.topic = meetingdata["topic"]

            content={
                    "MeetingURL": self.meetingURL, 
                    "password": self.meetingPassword,
                    "meetingTime": self.meetingTime,
                    "Purpose": self.topic,
                    "message": "Success"
                    }
            return self.statusOkay(content)   
        except:
            return self.serverError()
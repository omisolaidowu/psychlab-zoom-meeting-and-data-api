import requests
import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(sys.path[0] + "/..")
from errors.errorhandler import Errors
from models.models import MeetingDetail
from services.details import Details
from services.collectionDB import MakeCollection
from services.jsonEncode import JSONEncoder
from utils.convertdate import ConvertTime
from datetime import datetime


class CreateMeetingInfo(Details, Errors, ConvertTime):
    def __init__(self) -> None:
        self.client_id = os.getenv("CLIENT_ID")
        self.account_id = os.getenv("ACCOUNT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.auth_token_url = os.getenv("OAUTH_TOKEN_URL")
        self.api_base_url = os.getenv("API_BASE_URL")
        self.collection = MakeCollection()
        self.meetingdetails = None
        self.meetingURL: str
        self.meetingPassword: str
        self.meetingTime: str
        self.topic: str
        self.access_token: str
        self.duration: str
        self.state = "Upcoming"
        self.current_date_time = datetime.now()
        # Extract and print the day of the month
        self.day_of_month = self.current_date_time.day

    
    def create_meeting(self, meet: MeetingDetail):

        data = {
        "grant_type": "account_credentials",
        "account_id": self.account_id,
        "client_secret": self.client_secret
    }
        response = requests.post(self.auth_token_url, auth=(self.client_id, self.client_secret), data=data)
        if response.status_code!=200:
            return self.verificationError("Unable to get access token")
        response_data = response.json()
        access_token = response_data["access_token"]

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "topic": meet.topic,
            "duration": meet.duration,
            'start_time': f'{meet.start_date}T10:{meet.start_time}',
            "type": 2
        }
        resp = requests.post(f"{self.api_base_url}/users/me/meetings", headers=headers, json=payload)
        
        response_data = resp.json()

        self.meetingURL = response_data["join_url"]
        self.meetingPassword = response_data["password"]
        self.meetingTime = response_data["start_time"]
        self.topic = response_data["topic"]
        self.duration = response_data["duration"]

        content={
                    "meeting_url": self.meetingURL, 
                    "password": self.meetingPassword,
                    "meetingTime": self.convert_date_format(self.meetingTime),
                    "time": meet.start_time,
                    "purpose": self.topic,
                    "duration": self.duration,
                    "therapist_name": meet.therapist_name,
                    "therapist_email": meet.therapist_email,
                    "client_name": meet.client_name,
                    "client_email": meet.client_email,
                    "platform": "Zoom",
                    "message": "Success",
                    "state": self.state,
                    "updated_at": str(self.current_date_time),
                    "status":1
                                    }
        
        self.InsertedData = JSONEncoder().encode(content)

        user_meetings = eval(self.InsertedData)
        
        self.collection.insertuserSchedules(user_meetings)

        return self.statusOkay(content)
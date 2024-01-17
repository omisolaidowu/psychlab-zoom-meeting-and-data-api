import requests
import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(sys.path[0] + "/..")
from errors.errorhandler import Errors
from queries.getQueries import Queries
from services.collectionDB import MakeCollection
from models.models import GetAllAppointment
from services.jsonEncode import JSONEncoder
from datetime import datetime

userCollection = MakeCollection()

class UserAppointments(Queries):
    def getAll(self, details: GetAllAppointment):
        current_date_time = datetime.now()
        # Extract and print the day of the month
        day_of_month = current_date_time.day

        all_appointments  = self.getCurrentUserMeetings(details.email, 15)
        for  appointment in all_appointments:
            start_date = appointment["meetingTime"]
            day_part = start_date.split(",")[1].split(" ")[1]

            meeting_day = int(day_part)

            if day_of_month == meeting_day:
                appointment["state"] = "Today"
            elif day_of_month > meeting_day :
                appointment["state"] = "Completed"

        return all_appointments
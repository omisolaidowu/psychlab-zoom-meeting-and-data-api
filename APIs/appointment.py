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
        current_day = current_date_time.day

        current_month = current_date_time.month

        all_appointments  = self.getCurrentUserMeetings(details.email, 15)
        for appointment in all_appointments:
            start_date = appointment["meetingTime"]
            # Parse the meeting date string to datetime object
            meeting_date = datetime.strptime(start_date, "%a, %d %b, %Y")
            # Extract the month and day components from the meeting date
            meeting_month = meeting_date.month
            meeting_day = meeting_date.day

            if current_month == meeting_month and current_day == meeting_day:
                # The appointment is scheduled for today
                appointment["state"] = "Today"
            elif current_month == meeting_month and current_day > meeting_day:
                # The appointment has already occurred
                appointment["state"] = "Completed"
            elif current_month > meeting_month:
                # The appointment was in a previous month
                appointment["state"] = "Completed"

        return all_appointments
    
    def getAllTherapist(self, details: GetAllAppointment):
        current_date_time = datetime.now()
        # Extract and print the day of the month
        current_day = current_date_time.day

        current_month = current_date_time.month

        all_appointments  = self.getCurrentTherapistMeetings(details.email, 15)
        for appointment in all_appointments:
            start_date = appointment["meetingTime"]
            # Parse the meeting date string to datetime object
            meeting_date = datetime.strptime(start_date, "%a, %d %b, %Y")
            # Extract the month and day components from the meeting date
            meeting_month = meeting_date.month
            meeting_day = meeting_date.day

            if current_month == meeting_month and current_day == meeting_day:
                # The appointment is scheduled for today
                appointment["state"] = "Today"
            elif current_month == meeting_month and current_day > meeting_day:
                # The appointment has already occurred
                appointment["state"] = "Completed"
            elif current_month > meeting_month:
                # The appointment was in a previous month
                appointment["state"] = "Completed"

        return all_appointments
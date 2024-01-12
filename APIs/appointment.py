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

userCollection = MakeCollection()

class UserAppointments(Queries):
    def getAll(self, details: GetAllAppointment):
        # query = {"Email": details.email}
        # current = self.getCurrentUser(query, userCollection.usercol)
        all_appointments  = self.getCurrentUserMeetings(details.email, 15)
        return all_appointments
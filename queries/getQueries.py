import sys
sys.path.append(sys.path[0] + "/..")
from services.collectionDB import MakeCollection
from errors.errorhandler import Errors
# from models.models import Sess

mkCollection = MakeCollection()

class Queries(Errors):
    def getTimes(self):       
        document = list(mkCollection.therapists.find({}, {'_id': 0}))
        return document
    
    def getDBDocs(self):     
        document = list(mkCollection.therapists.find({}, {'_id': 0}))
        return self.statusOkay(document)
    
    def queryTargetDay(self, emailAddress, name, days):
        query = {"email": emailAddress}
        data = list(mkCollection.therapists.find(query, 
        {'{}.{}'.format(name, days):1, "_id":0}))
        return data
    
    def queryDays(self, emailAddress):
        query = {"email": emailAddress}
        data = mkCollection.therapists.find_one(query)

        First_name = data.get("first_name")
        therapist_meetings = {
            "Email": data.get("email"),
            "First name": First_name,
            "Schedules": data.get(First_name)
        }
        return therapist_meetings
    
    def getCurrentUser(self, query, collection):
        usercollect = collection.find_one(query, 
                                {'Email':1, 
                                 "First_name":1, 
                                 "Last_name":1,
                                 "_id":1,
                                 "is_admin":1,
                                 "is_super_admin":1,
                                 "is_user":1,
                                 "message":"success"
                                 })
        return usercollect
    
    def getCurrUserStatus(self, query, collection):
        usercollect = collection.find_one(query, 
                                {'Email':1, 
                                 "is_verified":1,
                                 "_id":1
                                 })
        return usercollect
    
    def getallUsers(self):     
        document = list(mkCollection.usercol.find({}, {'_id': 0}))
        return self.statusOkay(document)
    
    def getCurrentUserMeetings(self, email: str, limit: int):
        meetings = list(mkCollection.meetings.find({"client_email": email}, {"_id": 0}).sort("updated_at").limit(limit))
        return meetings
    
    def delete_field_by_email(self, email):
        query = {"email": email}
        data = mkCollection.therapists.find_one(query)
        First_name = data.get("first_name")

        mkCollection.therapists.update_one(query, 
                                {"$set":{"{}".format(First_name):[]}})

        # mkCollection.therapists.update_many({},{'$pull':{'{}'.format(First_name):None}})

        # update = {"$set": {First_name: ""}}

        



    
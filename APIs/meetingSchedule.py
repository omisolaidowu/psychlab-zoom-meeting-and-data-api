import sys


sys.path.append(sys.path[0] + "/..")


from models.models import MeetingSchedules
from services.collectionDB import MakeCollection

from services.jsonEncode import JSONEncoder
from fastapi.responses import JSONResponse 

from bson import ObjectId

from errors.errorhandler import Errors



encode = JSONEncoder()

mkCollection = MakeCollection()


class WriteSchedule(Errors):

    def __init__(self) -> None:
        self.data = None

    def submitSchedule(self, schedule: MeetingSchedules):
        self.data = {
            "email":schedule.email,
            "user_id": ObjectId(),
            "name": schedule.name,
            schedule.name:[{schedule.days:schedule.scheduleTimes}]
        }
        try:

            self.data = JSONEncoder().encode(self.data)

            Mydata = eval(self.data)

            if mkCollection.therapists.count_documents(
                {'email': Mydata['email']}
                ) > 0:
                return self.therapistExists()
            
            else:
                
                mkCollection.insertMeeting(Mydata)
                return self.statusOkay(self.data)
        
        except:
            return self.serverError()
        
    def getDBDocs(self):
        
        document = list(mkCollection.therapists.find({}, {'_id': 0}))

        return document

        
    
    def updateSchedules(self, schedule: MeetingSchedules):
        new_data = {schedule.name: {schedule.days:schedule.scheduleTimes}}


        documents = self.getDBDocs()

        #get all days data:
        docs = documents[0][schedule.name]

        #get a list of all keys from the days data:
        filteredDates = [list(i.keys())[0] for i in docs]


        if schedule.days in filteredDates:
            return self.dayExists()
            
        else:
            mkCollection.therapists.update_many(
                            {'name': schedule.name}, 
                            {'$push': new_data}, 
                            upsert = True
                            )
            responsedata = mkCollection.therapists.find({}, {'_id': 0})
            
        
            return self.statusOkay(list(responsedata))
        


    
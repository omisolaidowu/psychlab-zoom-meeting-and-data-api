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
            "first_name": schedule.first_name,
            "last_name": schedule.last_name,
            "email":schedule.email,
            "user_id": ObjectId(),
            schedule.first_name:[{schedule.days:schedule.scheduleTimes}]
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
        
    def getTimes(self):
        
        document = list(mkCollection.therapists.find({}, {'_id': 0}))

        return document
    
    def getDBDocs(self):
        
        document = list(mkCollection.therapists.find({}, {'_id': 0}))

        return self.statusOkay(document)


    
    def updateSchedules(self, schedule: MeetingSchedules):
        new_data = {schedule.first_name: {schedule.days:schedule.scheduleTimes}}

        documents = self.getTimes()

        first_names = [i["first_name"] for i in documents]
        last_names = [i["last_name"] for i in documents]

        dates = [list(i.keys())[4] for i in documents]

        staffDateTrackIndex = dates.index(schedule.first_name)

        staffDates = [i for i in documents[staffDateTrackIndex][schedule.first_name]]

        filteredDates = [list(i.keys())[0] for i in staffDates]

        if schedule.days in filteredDates:
            return self.dayExists()
        if (
            schedule.first_name not in first_names
            or
            schedule.last_name not in last_names
            ):
            return self.noDataError()
        elif len(documents)<1:
            return self.noDataError()

        else:
            try:
                mkCollection.therapists.update_many(
                                {'last_name': schedule.last_name}, 
                                {'$push': new_data}, 
                                upsert = True
                                )
                responsedata = mkCollection.therapists.find({}, {'_id': 0})
                
            
                return self.statusOkay(list(responsedata))
            except KeyError as e:
                return self.serverError
        


    
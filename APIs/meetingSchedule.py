import sys


sys.path.append(sys.path[0] + "/..")


from models.models import MeetingSchedules, ReplacementData

from services.collectionDB import MakeCollection

from services.jsonEncode import JSONEncoder


from bson import ObjectId

from errors.errorhandler import Errors



encode = JSONEncoder()

mkCollection = MakeCollection()


class WriteSchedule(Errors):

    def __init__(self) -> None:
        self.data = None
        self.isDay = True

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
    
    def queryTargetDay(self, emailAddress, name, days):
        query = {"email": emailAddress}
        data = list(mkCollection.therapists.find(query, 
        {'{}.{}'.format(name, days):1, "_id":0}))

        return data


    
    def updateSchedules(self, schedule: MeetingSchedules):
        new_data = {schedule.first_name: {schedule.days:schedule.scheduleTimes}}

        documents = self.getTimes()
        try:

            dayData = self.queryTargetDay(schedule.email, schedule.first_name, schedule.days)

            dates = dayData[0][schedule.first_name]

            filter = [(list(i.keys())) for i in dates]

            self.isDay=True
        except KeyError as e:
            self.isDay = False
            print(e)
        

        first_names = [i["first_name"] for i in documents]
        last_names = [i["last_name"] for i in documents]

        selectedDay = [x for l in filter for x in l]

        if schedule.days in selectedDay:
            return self.dayExists()
        elif (
            schedule.first_name not in first_names
            or
            schedule.last_name not in last_names
            ):
            return self.noDataError()
        elif len(documents)<1:
            return self.noDataError()

        else:
            try:
                query = {"email": schedule.email}
                mkCollection.therapists.update_one(
                                query, 
                                {'$push': new_data}, 
                                upsert = True
                                )
                responsedata = mkCollection.therapists.find({}, {'_id': 0})



                return self.statusOkay(list(responsedata))
            except KeyError as e:
                return self.serverError
            
    def reduceTime(self, schedule: MeetingSchedules):
        query = {"email": schedule.email}
        try:

            p = self.queryTargetDay(schedule.email, schedule.first_name, schedule.days)

            dates = p[0][schedule.first_name]

            filter = [(list(i.keys())) for i in dates]

            dateIndex = filter.index([schedule.days])

            print(dates)
            

            if (len(filter)>=1):

                filteredTimes = dates[dateIndex][schedule.days]
                if not schedule.time in filteredTimes:
                    return self.timeSelectedError()  
                else:
                    mkCollection.therapists.update_one(query, 
                    {"$pull": {'{}.{}.{}'.format(schedule.first_name, dateIndex, schedule.days): schedule.time}})
                    

                    if (len(filteredTimes)==1):

                        mkCollection.therapists.update_one(query, 
                                {"$unset":{"{}.{}".format(schedule.first_name, dateIndex):""}})

                        mkCollection.therapists.update_many({},{'$pull':{'{}'.format(schedule.first_name):None}})
                        
                    return self.statusOkay(self.getTimes())

            else:
                print("Error")
                return self.serverError()
                
        except IndexError as e:
            print(e)
            return self.timeSelectedError()
        except ValueError as e:
            print(e)
            return self.timeSelectedError()
        except:
            return self.serverError()



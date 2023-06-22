import sys
sys.path.append(sys.path[0] + "/..")
from services.collectionDB import MakeCollection
from errors.errorhandler import Errors

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
    
    def getCurrentUser(self, query, collection):
        usercollect = collection.find_one(query, 
                                {'Email':1, 
                                 "First_name":1, 
                                 "Last_name":1,
                                 "_id":1,
                                 "is_admin":1,
                                 "is_super_admin":1,
                                 "is_user":1
                                 })
        return usercollect
    
    def getCurrUserStatus(self, query, collection):
        usercollect = collection.find_one(query, 
                                {'Email':1, 
                                 "is_verified":1,
                                 "_id":1
                                 })
        return usercollect
    
    def getLoggedUser(self, query, collection):
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
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
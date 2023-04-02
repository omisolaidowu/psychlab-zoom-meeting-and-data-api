import pymongo

import urllib 

import os

from dotenv import load_dotenv


load_dotenv()


class MakeCollection:
    def __init__(self) -> None:
        self.password = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD"))
        self.user = urllib.parse.quote_plus(os.getenv("MONGO_USERNAME"))
    
       
        client = pymongo.MongoClient(
            "mongodb+srv://{}:{}@cluster0.rpb1yuu.mongodb.net/?retryWrites=true&w=majority".format(
            self.user, self.password
            ))
        db = client.therapistDates
        self.therapists = db.therapists
        # self.doc = next(self.therapists)
    
    def insertMeeting(self, data):
        
        return self.therapists.insert_one(data)
            
        
        
    
        
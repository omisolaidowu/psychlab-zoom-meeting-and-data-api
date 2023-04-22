#Todo: New user registration API
from models.models import User
from utils.paswordHash import PasswordActions
from services.jsonEncode import JSONEncoder
from services.collectionDB import MakeCollection
from errors.errorhandler import Errors

userCollection = MakeCollection()

class Register(PasswordActions, Errors):
    def __init__(self) -> None:
        self.data = None

    def register(self, user: User):
        self.data = {
            "First_name": user.first_name,
            "Last_name": user.last_name,
            "Email": user.email,
            "Password": user.Password,
        }

        try:
            self.InsertedData = JSONEncoder().encode(self.data)

            Mydata = eval(self.InsertedData)

            if userCollection.usercol.count_documents(
                {'Email': Mydata['Email']}) > 0:
                return self.userExists()
            elif len(self.data["Password"])<8:
                return self.passwordShortError()
            
            else:
                Mydata["Password"] = self.get_password_hash(Mydata["Password"])
                userCollection.insertUser(Mydata)
                return self.statusOkay(list(Mydata))     
        except:
            return self.serverError()





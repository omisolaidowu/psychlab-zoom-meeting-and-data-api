#Todo: New user registration API
from models.models import User
from utils.paswordHash import PasswordActions
from services.jsonEncode import JSONEncoder
from services.collectionDB import MakeCollection
from errors.errorhandler import Errors
import re
from services.verificationlink import EmailVerification
from queries.getQueries import Queries
import os
from dotenv import load_dotenv
load_dotenv()

userCollection = MakeCollection()

class Register(Queries, EmailVerification, PasswordActions, Errors):
    def __init__(self) -> None:
        self.data = None
        self.regex = r'{}'.format(os.getenv("EMAIL_VALIDATION_REGEX"))

    def register(self, user: User):
        self.data = {
            "First_name": user.first_name,
            "Last_name": user.last_name,
            "Email": user.email,
            "Password": user.Password,
            "is_admin":"False",
            "is_super_admin":"False",
            "is_user":"True",
            "is_verified":"False",
        }
        self.InsertedData = JSONEncoder().encode(self.data)


        Mydata = eval(self.InsertedData)

        if userCollection.usercol.count_documents(
            {'Email': Mydata['Email']}) > 0:
            return self.userExists()
        elif len(self.data["Password"])<8:
            return self.passwordShortError()
        
        elif not (re.fullmatch(self.regex, Mydata['Email'])):
            return self.inValidEmail()
        else:
            
            Mydata["Password"] = self.get_password_hash(Mydata["Password"])

        if self.data["Email"] == os.getenv("SUPER_ADMIN_EMAIL"):
            Mydata["is_super_admin"] = "True"
            Mydata["is_admin"] = "True"
            
        userCollection.insertUser(Mydata)

        query = {"Email": Mydata["Email"]}
        current = self.getCurrentUser(query, userCollection.usercol)

        user_id = str(current["_id"])

        # self.sendVerificationLink(Mydata['Email'], user_id): Pending->Gmail option not good
        return self.statusOkay({"Message": "Registration successful! Please, verify your email by clicking the link sent to your email address"})     
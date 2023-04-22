from utils.getuser import userCheck
from datetime import timedelta
from services.collectionDB import MakeCollection
from dotenv import load_dotenv
from errors.errorhandler import Errors
import os
load_dotenv()
from models.models import LoginUserSchema


userCollection = MakeCollection()


class Login(userCheck, Errors):
    def login_for_access_token(self, login: LoginUserSchema):
        try:
            user = self.authenticate_user(userCollection.usercol, login.email, login.password)
            if not user:
                return self.userNotVerified()
            else:
                try:   
                    access_token_expires = timedelta(minutes= int(os.getenv("EXPIRE_MINUTES")))
                    access_token = self.create_access_token(
                        data={"sub": login.email}, expires_delta=access_token_expires
                    )
                    return {"access_token": access_token, "token_type": "bearer"}
                except:
                    self.userNotVerified()
        except:
            self.serverError()

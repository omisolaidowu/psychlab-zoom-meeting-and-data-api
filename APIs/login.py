from utils.authentication import userCheck
from datetime import timedelta
from services.collectionDB import MakeCollection
from dotenv import load_dotenv
from errors.errorhandler import Errors
import os
load_dotenv()
from models.models import LoginUserSchema, Token
from queries.getQueries import Queries
from queries.updates import queryupdates

userCollection = MakeCollection()

class Login(Queries, userCheck, Errors, queryupdates):
    def login_for_access_token(self, login: LoginUserSchema):
        # try:
        user = self.authenticate_user(userCollection.usercol, login.email, login.password)
        query = {"Email": login.email}
        current = self.getCurrentUser(query, userCollection.usercol)

        if not user:
            return self.userNotVerified()
        else:
            access_token_expires = timedelta(minutes=int(os.getenv("EXPIRE_MINUTES")))
            access_token = self.create_access_token(data={"sub": login.email}, expires_delta=access_token_expires)

            meetings = self.getCurrentUserMeetings(login.email, 3)

            token = Token(
                access_token = access_token, 
                token_type = "bearer", 
                role = "user",
                message = "success",
                first_name=current['First_name'],   
                sessions = meetings,
                status = 1
                            )

            if str(current["is_admin"])=="True":
                token = Token(
                    access_token=access_token, 
                    token_type="bearer", 
                    role="admin",
                    message="success",
                    first_name=current["First_name"],
                    status=1
                    )

            if str(current["is_super_admin"])=="True":
                token = Token(
                    access_token=access_token,
                    token_type="bearer", 
                    role="super_admin",
                    message="success",
                    first_name=current["First_name"],
                    status=1
                    )
                
            self.update_token(query, str(token.access_token), userCollection.usercol)

            return token
        # except:
        #     return self.serverError()
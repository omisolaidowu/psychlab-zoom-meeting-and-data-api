from errors.errorhandler import Errors
from dotenv import load_dotenv
from utils.authentication import userCheck
from services.collectionDB import MakeCollection
from models.models import User
from queries.getQueries import Queries
load_dotenv()

userCollection = MakeCollection()

class VerifyEmail(Queries, userCheck, Errors):
    def verify_email(self, user_id: str, currUser: User):
        try:
            query = {"Email": currUser.email}
            user = self.getCurrUserStatus(query, userCollection.usercol)
            if not user:
                return self.notFoundError("User not found...")
            elif user_id != str(user["_id"]):
                return self.notFoundError("User not found or invalid verification link...")
            elif user["is_verified"] == "True":
                return {"message": "Email already verified"}
            else:
                userCollection.usercol.update_one(
            {"Email": currUser.email}, {"$set": {"is_verified": "True"}}
            )
                return self.statusOkay({"user_id": user_id, "message": "Email verified successfully"})
        except TypeError:
            return self.notFoundError("User not found...")
        except:
            return self.serverError()
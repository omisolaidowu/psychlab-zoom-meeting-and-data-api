from queries.getQueries import Queries
from errors.errorhandler import Errors
from models.models import TokenDelete
from services.collectionDB import MakeCollection
import json

collection = MakeCollection()


class GetUserInfo(Queries, Errors):
    def get_user_info(self, token: TokenDelete):
        query = {"access_token": token.token}
        current_user = self.getCurrentUser(query, collection.usercol)

        content = {
            "email": str(current_user["Email"]),
            "first_name": str(current_user["First_name"]),
            "last_name": str(current_user["Last_name"]),
            "message":"success",
            "status":1
        }
        return content
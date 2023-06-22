from queries.updates import queryupdates
from models.models import TokenDelete
from services.collectionDB import MakeCollection
from errors.errorhandler import Errors

collection = MakeCollection()


class DeleteToken(queryupdates, Errors):
    def delete_token(self, token: TokenDelete):
        query = {"access_token": token.token}
        self.delete_access_token(query, collection.usercol)
        return self.statusOkay("Token removed successfully after logout")
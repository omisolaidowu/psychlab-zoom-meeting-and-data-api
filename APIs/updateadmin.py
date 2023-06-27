from queries.updates import queryupdates
from errors.errorhandler import Errors
from services.collectionDB import MakeCollection
from models.models import AdminUpdate

collection = MakeCollection()

class UpdateToAdmin(queryupdates, Errors):

    def update_to_admin(self, admin: AdminUpdate):

        query = {"Email": admin.email}

        self.update_user_to_admin(query, admin.is_admin, collection.usercol)

        return self.statusOkay("User role updated successfully")






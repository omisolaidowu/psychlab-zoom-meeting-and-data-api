from queries.getQueries import Queries

from errors.errorhandler import Errors

class GetAllUsers(Queries, Errors):
    def getusers(self):
        return self.getallUsers()


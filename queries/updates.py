class queryupdates:
    def updateWithAccessToken(self, query, AccessToken, collection):  
        collection.update_one(
                         query, 
                        {'$push': AccessToken}, 
                                )
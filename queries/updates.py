class queryupdates:
    def updateWithAccessToken(self, query, AccessToken, collection):  
        collection.update_one(
                         query, 
                        {'$push': AccessToken}, 
                                )
    def update_token(self, query, AccessToken, collection):
        update = {'$set': {'access_token': AccessToken}}

        collection.update_one(query, update)

    def delete_access_token(self, query, collection):

        update = {'$unset': {'access_token': 1}}

        collection.update_one(query, update)

    def update_user_to_admin(self, query, value, collection):
        
        update = {'$set': {'is_admin': value}}

        collection.update_one(query, update)


    def update_user_to_superadmin(self, query, value, collection):
        
        update = {'$set': {'is_super_admin': value}}

        collection.update_one(query, update)
from models.models import User
from services.collectionDB import MakeCollection
from utils.paswordHash import PasswordActions
from datetime import datetime, timedelta
import os
from jose import jwt
from errors.errorhandler import Errors
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

load_dotenv()

userCollection = MakeCollection()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class userCheck(PasswordActions, Errors):
    def get_user(self, collection, email:str):
        query = {"Email": email}
        usercollect = collection.find_one(query, {'Email':1, "Password":1, "_id":0})
        try:
            if not email == usercollect["Email"]:
                return self.userNotVerified()
                
            else:
                return usercollect
                
        except:
            return self.userNotVerified()
    
    def authenticate_user(self, collection, email: str, password: str):
        user = self.get_user(collection=collection, email=email)
        try:
            if not user:
                return False
            if not self.verify_password(password, user["Password"]):
                return False
            else:
                return user
        except:
            self.userNotVerified()

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
            to_encode = data.copy()
            if expires_delta:
                expire = datetime.utcnow() + expires_delta
            else:
                expire = datetime.utcnow() + timedelta(
                minutes= int(os.getenv("EXPIRE_MINUTES"))
                )
            to_encode.update({"exp": expire})
            encoded_jwt = jwt.encode(
            to_encode, os.getenv("JWT_SECRET_KEY"), algorithm=os.getenv("ALGORITHM")
            )
            return encoded_jwt
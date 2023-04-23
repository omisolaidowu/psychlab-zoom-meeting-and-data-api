import sys
sys.path.append(sys.path[0] + "/..")

from APIs.zoomConnect import CreateMeetingInfo
from APIs.meetingSchedule import WriteSchedule
from APIs.register import Register
from APIs.login import Login
from models.models import Token
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from APIs.emailvefication import VerifyEmail

load_dotenv()

import uvicorn

meetingInfo = CreateMeetingInfo()

writemeeting = WriteSchedule()

registration = Register()

token = Login()

verifyemail = VerifyEmail()

origins = [
    "http://localhost:5000",
]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


router = APIRouter()

router.add_api_route('/api/get-data', 
endpoint = writemeeting.getDBDocs, methods=["GET"])


router.add_api_route('/api/create-zoomlink', 
endpoint = meetingInfo.createMeeting, methods=["POST"])

router.add_api_route('/api/create-schedule', 
endpoint = writemeeting.submitSchedule, methods=["POST"])


router.add_api_route('/api/remove-selected-time', 
endpoint = writemeeting.reduceTime, methods=["POST"])


router.add_api_route('/api/update-schedule', 
endpoint = writemeeting.updateSchedules, methods=["PUT"])

router.add_api_route('/api/register', 
endpoint = registration.register, methods=["POST"])

router.add_api_route('/api/login', response_model=Token,
endpoint =token.login_for_access_token , methods=["POST"])

router.add_api_route('/api/verify-email/{user_id}',
endpoint =verifyemail.verify_email , methods=["PUT"])

app.include_router(router)

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
from fastapi.responses import JSONResponse 


class Errors:
    def therapistExists(self):
        return JSONResponse(
                status_code=400, 
                content={
            "status": 0,
            "message": "Therapist already exists" })
    def noDataError(self):
        return JSONResponse(
                status_code=403, 
                content={
            "status": 0,
            "message": "Please add data before updating" })
    def dayExists(self):
        return JSONResponse(
                status_code=400, 
                content={
            "status": 0,
            "message": "Duplicate dates not allowed for one therapist" })
    
    def timeSelectedError(self):
        return JSONResponse(
                status_code=400, 
                content={
            "status": 0,
            "message":
        "Error! Someone else might've booked this time while you left off.\
              Please select another time or other therapists" })
    
    def serverError(self):
        return JSONResponse(
                status_code=500, 
                content={
            "status": 0,
            "message": "An error occured, please try again" })
    def statusOkay(self, response):
        return JSONResponse(
                status_code=200, 
                content={
                        "data": response,
                        "message": "Success",
                        "status":1
                            })

    def submittedSuccess(self, response):
        return JSONResponse(
                status_code=200, 
                content={
                        "data": response,
                        "message": 
                        "Meeting scheduled successfully.\
                            Please check your email for meeting link.",
                        "status":1
                            })





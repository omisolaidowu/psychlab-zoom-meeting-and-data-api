from fastapi.responses import JSONResponse 


class Errors:
    def therapistExists(self):
        return JSONResponse(
                status_code=400, 
                content={"message": "Therapist already exists" })
    def dayExists(self):
        return JSONResponse(
                status_code=400, 
                content={"message": "Duplicate dates not allowed for one therapist" })
    def serverError(self):
        return JSONResponse(
                status_code=500, 
                content={"message": "An error occured, please try again" })
    def statusOkay(self, response):
        return JSONResponse(
                status_code=200, 
                content={
                        "data": response,
                        "message": "Success"
                            })





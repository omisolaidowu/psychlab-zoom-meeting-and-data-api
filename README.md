# Psycho-Therapy Booking Web Application API

This API is built using Python's FastAPI and MongoDB as the database. 

### This API is still under development but it currently handles the following endpoints:

* User registration endpoint
* User authentication (Login) endpoint
* User email verification endpoint
* Zoom Meeting Link Generation endpoint
* Admin date and time meeting scheduling endpoint; built using custom-designed data structure
* Successive date and time removal endpoint for each scheduled time and date
* Schedule update

## Codebase Structure
```
PsychLab_API
├─ .gitignore
├─ APIs
│  ├─ emailvefication.py
│  ├─ login.py
│  ├─ meetingSchedule.py
│  ├─ register.py
│  └─ zoomConnect.py
├─ errors
│  └─ errorhandler.py
├─ models
│  └─ models.py
├─ queries
│  ├─ getQueries.py
│  └─ updates.py
├─ requirements.txt
├─ router
│  └─ main.py
├─ services
│  ├─ collectionDB.py
│  ├─ details.py
│  ├─ jsonEncode.py
│  └─ verificationlink.py
└─ utils
   ├─ authentication.py
   ├─ paswordHash.py
   └─ __init__.py
```
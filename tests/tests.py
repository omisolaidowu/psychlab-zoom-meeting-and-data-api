import unittest
from fastapi.testclient import TestClient
import sys
sys.path.append(sys.path[0] + "/..")
from router.main import app

client = TestClient(app)

class TestAPIs(unittest.TestCase):

    def test_get_data(self):
        response = client.get("/api/get-data")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_create_zoomlink(self):
        payload = {
            "topic": "Test Meeting",
            "start_time": "2022-01-01T12:00:00Z",
            "duration": 60
        }
        response = client.post("/api/create-zoomlink", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("join_url", response.json())

    def test_create_schedule(self):
        payload = {
            "user_id": "testuser",
            "schedule": [
                {
                    "date": "2022-01-01",
                    "timeslots": [
                        "12:00 PM",
                        "1:00 PM",
                        "2:00 PM"
                    ]
                },
                {
                    "date": "2022-01-02",
                    "timeslots": [
                        "3:00 PM",
                        "4:00 PM",
                        "5:00 PM"
                    ]
                }
            ]
        }
        response = client.post("/api/create-schedule", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("schedule_id", response.json())

    def test_remove_selected_time(self):
        payload = {
            "schedule_id": "testschedule",
            "date": "2022-01-01",
            "time": "12:00 PM"
        }
        response = client.post("/api/remove-selected-time", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.json())

    def test_update_schedule(self):
        payload = {
            "schedule_id": "testschedule",
            "schedule": [
                {
                    "date": "2022-01-01",
                    "timeslots": [
                        "1:00 PM",
                        "2:00 PM"
                    ]
                },
                {
                    "date": "2022-01-02",
                    "timeslots": [
                        "4:00 PM",
                        "5:00 PM"
                    ]
                }
            ]
        }
        response = client.put("/api/update-schedule", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.json())

    def test_register(self):
        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        }
        response = client.post("/api/register", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())

    def test_login(self):
        payload = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = client.post("/api/login", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())

    def test_verify_email(self):
        response = client.put("/api/verify-email/testuser")
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.json())

if __name__ == '__main__':
    unittest.main()
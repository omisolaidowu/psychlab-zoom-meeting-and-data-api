

class Details:

    def meetDetails(self, details):
            self.meetingdetails = {
                            "topic": "Pyschological Evaluation",
                            "type": 2,
                            "start_time": details,
                            "duration": "120",
                            "timezone": "Africa/Nigeria",
                            "agenda": "test",
            
                            "recurrence": {"type": 1,
                                            "repeat_interval": 1
                                            },
                            "settings": {"host_video": "true",
                                        "participant_video": "true",
                                        "join_before_host": "False",
                                        "mute_upon_entry": "False",
                                        "watermark": "true",
                                        "audio": "voip",
                                        "auto_recording": "cloud"
                                        }
                            }
            return self.meetingdetails
        
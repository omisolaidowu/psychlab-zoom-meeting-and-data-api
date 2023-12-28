import requests
import os
from errors.errorhandler import Errors
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SMTP_API_KEY")
domain = os.getenv("SMTP_DOMAIN")

class SendEMail(Errors):
    def send_email(self, sender, recipient, subject, body):
        payload = {
        'from': sender,
        'to': recipient,
        'subject': subject,
        'html': body
        }
        response = requests.post(
        f'https://api.mailgun.net/v3/{domain}/messages',
        auth=('api', api_key),
        data=payload
        )
        if response.status_code == 200:
            return self.statusOkay("Email sent successfully!")
        else:
            return self.verificationError(
                'Failed to send email. Status code:', response.status_code
                )

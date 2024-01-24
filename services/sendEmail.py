import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("ELASTIC_EMAIL_API")

class SendEmail:
    def sendMail(self, client_email, therapist_email, company_email, client_name):

        # Elastic Email API endpoint for sending emails
        api_url = 'https://api.elasticemail.com/v2/email/send'

        company_email = 'omisolaesther@megapsychetherapy.com'

        # Email parameters
        from_email = company_email
        to_email = f'{client_email}, {therapist_email}, {company_email}'
        subject = f'New meeting with {client_email}'
        body_text = 'Hello, this is the email body.'

        # Construct the payload
        payload = {
            'apikey': api_key,
            'from': from_email,
            'to': to_email,
            'subject': subject,
            'body_text': body_text,
        }

        # Send the HTTP request
        response = requests.post(api_url, data=payload)

        # Check the response
        if response.status_code == 200:
            print('Email sent successfully!')
        else:
            print(f'Error sending email. Status code: {response.status_code}, Response content: {response.text}')
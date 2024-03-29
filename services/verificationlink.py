from utils.send_emails import SendEMail
from errors.errorhandler import Errors
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()

sender_email = os.getenv("SMTP_EMAIL_TEMPORARY")

class EmailVerification(SendEMail, Errors):

    def sendVerificationLink(self, recipient_email, user_id):
        try:
            subject = 'MegaPsychLab Verification Link'
            url = "http://localhost:5000/api/verify-email/{}".format(user_id)
            body = """ 
            <strong>Please click the link below to verify your email address</strong>
            <h2><a href={}>Verify Email</a></h2>
            """.format(url)
            self.send_email(sender_email, 
                            recipient_email, 
                            subject, 
                            body
                            )
            return self.statusOkay()
        except:
            return self.verificationError("Failed to send email")
    







        # subject = 'MegaPsychLab Verification Link'
        # recipient_email = email
        # url = "http://localhost:5000/api/verify-email/{}".format(user_id)

        # body = """ 
        # <strong>Please click the link below to verify your email address</strong>
        # <h2><a href={}>Verify Email</a></h2>
        # """.format(url)

        # smtp_server = 'smtp.mailgun.org' 
        # port = 587 
        # sender_email = os.getenv("SMTP_EMAIL_TEMPORARY")
        # sender_password = os.getenv("SMTP_PASSWORD")


        # msg = MIMEMultipart()
        # msg['From'] = sender_email
        # msg['To'] = recipient_email
        # msg['Subject'] = subject
        # msg.attach(MIMEText(body, 'HTML'))

        # with smtplib.SMTP(smtp_server, port) as server:
        #     server.starttls()
        #     server.login(sender_email, sender_password)
        #     text = msg.as_string()
        #     server.sendmail(sender_email, recipient_email, text)
        #     return self.statusOkay("Email verified successfully!")
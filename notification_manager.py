from twilio.rest import Client
import smtplib
import os

# loads an .env file to load sensitive data from it
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL_ENV")
MY_PASSWORD = os.environ.get("MY_PASSWORD_ENV")


class NotificationManager:

    # sends an SMS with the message passed to the function
    def send_sms(self, message):
        account_sid = f'{os.environ.get("ACCOUNT_SID_ENV")}'
        auth_token = f'{os.environ.get("AUTH_TOKEN_ENV")}'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=f'+{os.environ.get("FROM_ENV")}',
            body=f'{message}',
            to=f'+{os.environ.get("TO_ENV")}'
        )

        print(message.sid)

    def send_email(self, data, message):
        with smtplib.SMTP('outlook.office365.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for user in data:
                email = user['email']
                name = user['firstName']
                try:
                    connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                        msg=f'Subject::New Low Price Flight!!\n\nHey {name},\n{message}'.encode(
                                            'utf-8'))
                except:
                    print(f'Wrong mail: {email}')
                    continue

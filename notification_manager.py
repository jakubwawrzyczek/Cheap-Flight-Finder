from twilio.rest import Client
import os

# loads an .env file to load sensitive data from it
from dotenv import load_dotenv

load_dotenv()


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

import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def send_message(number, body):
    message = client.messages.create(
        body=body,
        messaging_service_sid='MG7e631beba521ce722b8b3b6911ba53d8',
        to=number
    )
    print(message.sid)


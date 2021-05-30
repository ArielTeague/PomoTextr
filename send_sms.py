import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
mess_id = os.environ['MESS_SERVICE_SID']
client = Client(account_sid, auth_token)


def send_message(number, body):
    message = client.messages.create(
        body=body,
        messaging_service_sid=os.environ['MESS_SERVICE_SID'],
        to=number
    )

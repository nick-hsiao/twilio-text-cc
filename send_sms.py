from twilio.rest import Client
import os
# Your Account SID from twilio.com/console


account_sid = os.environ.get('TWILIO_ID')
# Your Auth Token from twilio.com/console
auth_token  = os.environ.get('TWILIO_AUTH')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=os.environ.get('MY_NUMBER'), 
    from_=os.environ.get('TWILIO_NUMBER'),
    body="Hello from Nick")

print(message.sid)
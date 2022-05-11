from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from phone_numbers import number_list
app = Flask(__name__)

account_sid = os.environ.get('TWILIO_ID')
auth_token  = os.environ.get('TWILIO_AUTH')
client = Client(account_sid, auth_token)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    body = request.values.get('Body')

    forward_sms(body)
    
    return Response(str(resp),mimetype="application/xml")

def forward_sms(msg):
    
    for number in number_list:

        client.messages.create(
        to=number, 
        from_=os.environ.get('TWILIO_NUMBER'),
        body=msg)


if __name__ == "__main__":
    app.run(debug=True)
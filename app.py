from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    
    resp.message("Hi there")
    

    return Response(str(resp),mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)
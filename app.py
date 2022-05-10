from flask import Flask, Response, request
from twilio import twiml

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    number = request.form['From']
    body = request.form['Body']
    
    resp = twiml.Response()
    print(body)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
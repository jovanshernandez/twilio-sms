from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_cheers_reply():
    """Respond to incoming messages with SMS."""
    # Start our repsonse to incoming messages
    resp = MessagingResponse()

    # Add a message
    resp.message("As you wish. You shall wake up in your bed as if nothing ever happened.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


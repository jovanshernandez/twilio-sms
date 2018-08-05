# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client


# Your account SID and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token_here'
client =  Client(account_sid, auth_token)

# Change the body, from, and to fields to whatever you want or need.
message = client.messages.create(
				body='Hello, world!',
				from_='[+][country_code][your_twilio_number_here]',
				to='[+][country_code][target_number]',
			)

print(message.sid)


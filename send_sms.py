# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client


# Your account SID and Auth Token from twilio.com/console
account_sid = 'AC202b5d1de5e90340b6b0c7dc628d595b'
auth_token = '1f53509d240fc4d95fa85f9767e78796'
client =  Client(account_sid, auth_token)

message = client.messages.create(
				body='Do you want to take the red pill, or blue pill?',
				from_='[+][1][6105107306]',
				to='[+][1][6105976107]',
			)

print(message.sid)


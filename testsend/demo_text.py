
# import required module
from twilio.rest import Client
import os

accountsid=os.environ.get('ACCOUNT_SID')
authenticationtoken=os.environ.get('AUTH_TOKEN')


try:
    client=Client(accountsid,authenticationtoken)

    message = client.messages.create(
            body="Hello, this is a test message",
            to="+919887381178",
            from_="+15746269040"
        )
    print(message.sid)
    print('Done')
except:
    print('Not done')
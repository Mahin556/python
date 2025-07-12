from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
recipient_number = os.getenv("RECEPIENT_NUMBER")

# Create Twilio client
client = Client(account_sid, auth_token)

# Send SMS
# in body part you have to write your message
message = client.messages.create(
    body='This is a new message',
    from_=twilio_number,
    to=recipient_number
)

print(f"Message sent with SID: {message.sid}")
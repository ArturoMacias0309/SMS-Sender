# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACd76a595dcd2e7f88d5195be44049ad13"
auth_token = "e9b33882c8e2c816d2ca6b326f49b1f1"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="TE AMO LOML",
  from_="+15855221061",
  to="+524493125397"
)
print(message.sid)
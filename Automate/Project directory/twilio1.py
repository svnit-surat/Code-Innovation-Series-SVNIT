
from twilio.rest import Client
from frontend1 import twiliowindow
from frontend1 import window3

#providing twilio service


client = Client(twiliowindow.account_sid.get(),  twiliowindow.auth_token.get())
def twilionotify():
    message = client.messages.create(
        from_=twiliowindow.twilio_num.get(),
        body=f"you have a class in {window3.notifytime.get()} minutes,get ready for it!",
        to=twiliowindow.phone_no.get()
    )




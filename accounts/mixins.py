
from django.conf import settings
from twilio.rest import Client


class MessageHandler:
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_on_phone(self):
        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(settings.ACOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages.create(
            body=f'your otp is {self.otp}',
            from_='+12092192290',
            to=self.phone_number
        )

        print(message.sid)
    print('msg testing from account mixin pending otp')

from twilio.rest import Client

TWILIO_DETAILS = {
    'account_sid': '',
    'auth_token': '',
    'number': ''

}


def send_message(phone_no='', message_body=''):
    """
    phone_no = '' - is the Phone number I used to verify my Twilio account
    for now I can only send text message to this number
    :param phone_no: receivers phone number
    :param message_body: message body
    :return: nothing for now
    """
    client = Client(TWILIO_DETAILS['account_sid'], TWILIO_DETAILS['auth_token'])

    # Phone number given to you by Twilio
    # all message will come from this number
    message_body = '\n' + message_body
    client.messages.create(to=phone_no, from_=TWILIO_DETAILS['number'], body=message_body)


send_message('', 'test')
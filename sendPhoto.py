import datetime
from envelopes import Envelope
from passwords import password

sender_email = "liam_simpkin@yahoo.com"
receiver_email = "liam_simpkin@yahoo.com"
messageSubject = "Does this still work? External password"
messageBody = "Your macbook pro loged in at" + str(datetime.datetime.now())
attachment = "./img/mugShot.png"

# creates email object
envelope = Envelope(
    from_addr=(sender_email, u'MacBook Login'),
    to_addr=(receiver_email, u'Me'),
    subject=messageSubject,
    text_body=messageBody
)
envelope.add_attachment('./img/mugShot.png')

# Send the envelope using an ad-hoc connection...
envelope.send('smtp.mail.yahoo.com', login='liam_simpkin@yahoo.com',
              password=password, tls=True)
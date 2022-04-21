#** imports app password for my Yahoo email account
# Replace this with input("Type your password and then press enter: ")
from passwords import password
import smtplib, ssl, datetime

port = 465  # For SSL
sender_email = "liam_simpkin@yahoo.com"
receiver_email = "liam_simpkin@yahoo.com"
message = """\
Subject: Epic login notification
Your macbook pro loged in at """ + str(datetime.datetime.now())

# Create a secure SSL context
context = ssl.create_default_context()
try :
  with smtplib.SMTP_SSL("smtp.mail.yahoo.com", port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
      print("Email sent!")
except:
  print ('can\'t send the Email')
  
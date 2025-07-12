import smtplib
from dotenv import load_dotenv
import os

load_dotenv() # This loads the variables from .env into the environment
email=os.getenv("EMAIL")
password=os.getenv("PASSWORD")
receiver_email="<your_email>"

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(email, password)

# message to be sent
message = "Hello Bhai kesa heeeee?"

# sending the mail
s.sendmail(email, receiver_email, message)

# terminating the session
s.quit()

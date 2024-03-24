import dotenv
dotenv.load_dotenv()
import aiosmtplib
import asyncio

import os
from email.message import EmailMessage

email_sender = "mynewsletters8429@gmail.com"
password = os.getenv("PASSWORD")
email_receiver = "amaanrizvi73@gmail.com"

subject = "This is a test"
body = "This is a test email"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

async def send_mail():
    await aiosmtplib.send(
    message=em,
    hostname="smtp.gmail.com",
    port=465,
    username=email_sender,
    password=password,
    use_tls=True,
)


asyncio.run(send_mail())
 


        


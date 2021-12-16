# IMPORTS 
import os 
import smtplib
from email.message import EmailMessage
from .passkey import pkey

# CONFIGS (email)
EMAIL_ADDRESS = 'YOUR EMAIL ADDRESS'
EMAIL_PASSWORD = pkey

def sendEmail(sendm, us, pw):
    msg = EmailMessage()
    msg['Subject'] = 'YOUR SUBJECT'
    msg['From'] = 'YOUR EMAIL ADDRESS'
    msg['To'] = sendm
    msg.set_content('Username: '+ us + '\n' +
        'Password: ' + pw)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
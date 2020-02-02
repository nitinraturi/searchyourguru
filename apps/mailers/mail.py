from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse_lazy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from django.conf import settings
from apps.users.tokens import *


def send_mail(receiver_email,subject,message):
    smtp_server = settings.EMAIL_HOST
    port = settings.EMAIL_PORT  # For starttls
    sender_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    html_body = MIMEText(message, 'html')
    msg.attach(html_body)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, msg.as_string())
        # print("mail sent")
    except Exception as e:
        # Print any error messages to stdout
        print("Mail error",e)
        print(receiver_email,sender_email,password)
    finally:
        server.quit()

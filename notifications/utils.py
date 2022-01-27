import json
import sys
import random
import requests
from django.core.mail import EmailMultiAlternatives, send_mail, EmailMessage
from django.conf import settings
from django.core import mail
import json
import slack

# def sendMail(net_amount_payable, amount_paid, order_id):
		
# 	send_async_email(subject, message, sender, receivers)	


def send_async_email(subject, message, sender, receivers, fail_silently=False):
    res = send_mail(
        subject,
        message,
        sender,
        receivers,
        fail_silently=fail_silently
    )
    print(f"{res} emails sent.")


def sendSlackMessage(message):
    client = slack.WebClient(token=settings.SLACK_TOKEN)
    print(client, "clientttttttttttttttttt")
    client.chat_postMessage(channel='general', text=message)

    return True

    
    
#!/usr/bin/env python3
import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient


def send_welcome(email, username, template_id):
    """ Send a dynamic email to a list of email addresses
    :returns API response code
    :raises Exception e: raises an exception """

    # from address we pass to our Mail object
    FROM_EMAIL = 'pieter@pieterkdevilliers.co.uk'

    # update to your dynamic template id from the UI
    TEMPLATE_ID = template_id

    # list of emails and preheader names, update with yours
    TO_EMAILS = [(email, username)]
        
        
    # create Mail object and populate
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAILS)
    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        'username': username
    }

    message.template_id = TEMPLATE_ID

    # create our sendgrid client object, pass it our key, then send and return our response objects
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        code, body, headers = response.status_code, response.body, response.headers
        print(f"Response code: {code}")
        print(f"Response headers: {headers}")
        print(f"Response body: {body}")
        print("Dynamic Messages Sent!")
    except Exception as e:
        print("Error: {0}".format(e))
    return str(response.status_code)
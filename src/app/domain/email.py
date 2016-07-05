""" Email domain object """
import logging

import sendgrid

from settings import SENDGRID_API_KEY, APP_URL


class Emailer(object):
    """
    Emailer class for wrapping up email functionality.
    """
    def __init__(self):
        self.sendgrid_client = sendgrid.SendGridClient(SENDGRID_API_KEY)

    def send_new_purchase_email(self, to_address, full_name, survey_type, user_id):
        survey_link = '{}/gifts/'.format(APP_URL)
        if survey_type == 'Short Survey A':
            survey_link += 'a/'
        elif survey_type == 'Short Survey B':
            survey_link += 'b/'
        survey_link += '?userId={}'.format(user_id)

        message = sendgrid.Mail()
        message.add_to('{} <{}>'.format(full_name, to_address))
        message.set_subject('Your Spiritual Gifts Survey is waiting')
        message.set_html("""
            <h1>Your Spiritual Gifts Survey Link</h1>
            <p>Click <a href="{survey_link}" target="_blank">here to go to your survey</a>.</p>
            <p>Thanks again for your purchase and have a great day!</p>
        """.format(survey_link=survey_link))
        message.set_text("Copy this link into your browser to go to the survey: {}".format(survey_link))
        message.set_from("Spiritual Gifts Survey <giftsurvey@holtscomm.ca>")
        try:
            self.sendgrid_client.send(message)
        except Exception as e:
            logging.info('Request to sendgrid failed, are you connected to the Internet?')

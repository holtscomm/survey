""" Email domain object """
import sendgrid

from settings import SENDGRID_API_KEY


class Emailer(object):
    """
    Emailer class for wrapping up email functionality.
    """
    def __init__(self):
        self.sendgrid_client = sendgrid.SendGridClient(SENDGRID_API_KEY)

    def send_new_purchase_email(self, to_address, full_name):
        message = sendgrid.Mail()
        message.add_to('{} <{}>'.format(full_name, to_address))
        message.set_subject('Thank you for purchasing the Survey!')
        message.set_html('Thanks')
        message.set_text('Thanks')
        message.set_from('Us <contact@holtscomm.ca>')
        self.sendgrid_client.send(message)

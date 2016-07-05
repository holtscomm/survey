""" purchase.py """
import datetime

from app.domain.email import Emailer
from app.models.user import User


class Purchase(object):
    """ Purchase domain object """
    def __init__(self, purchase_body):
        self.purchase_body = purchase_body

    @property
    def full_name(self):
        if self.first_name != '' and self.last_name == '':
            return self.first_name
        elif self.first_name == '' and self.last_name != '':
            return self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    @property
    def product(self):
        return (self.purchase_body.get('cart_details[0][name]') or self.purchase_body.get('cart_details[0][name][]'))[0]

    @property
    def purchase_date(self):
        return self.purchase_body.get('date', datetime.datetime.utcnow())

    @property
    def email(self):
        return self.purchase_body['email'][0]

    @property
    def first_name(self):
        return self.purchase_body['user_info[first_name]'][0]

    @property
    def last_name(self):
        return self.purchase_body['user_info[last_name]'][0]


def create_new_premium_user(purchase_object):
    """ Create a new user that has paid for the survey """
    return User.create(
        email=purchase_object.email,
        first_name=purchase_object.first_name,
        last_name=purchase_object.last_name,
        paid=True
    )


def send_email_with_survey_link(user_email, user_full_name, survey_type, user_id):
    """ Sends an email to a user telling them to take their new survey """
    emailer = Emailer()
    emailer.send_new_purchase_email(user_email, user_full_name, survey_type, user_id)

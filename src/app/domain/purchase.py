""" purchase.py """


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
        return self.purchase_body['cart_details[0][name]'][0]

    @property
    def purchase_date(self):
        return self.purchase_body['date'][0]

    @property
    def email(self):
        return self.purchase_body['email'][0]

    @property
    def first_name(self):
        return self.purchase_body['user_info[first_name]'][0]

    @property
    def last_name(self):
        return self.purchase_body['user_info[last_name]'][0]
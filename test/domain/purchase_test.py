""" Tests for the purchase domain module """
import unittest

from app.domain.purchase import Purchase


class PurchaseTests(unittest.TestCase):
    def setUp(self):
        super(PurchaseTests, self).setUp()
        self.PURCHASE_DICT = {
            'cart_details[0][name]': ['Short B Survey'],
            'date': ['whatever'],
            'email': ['graham@holtslander.com'],
            'user_info[first_name]': ['Graham'],
            'user_info[last_name]': ['Holtslander']
        }
        self.purchase = Purchase(self.PURCHASE_DICT)

    def test_full_name_is_first_and_last_if_both_exist(self):
        self.assertEqual('Graham Holtslander', self.purchase.full_name)

    def test_full_name_is_just_first_name_if_only_has_first_name(self):
        self.PURCHASE_DICT['user_info[last_name]'][0] = ''
        self.assertEqual('Graham', self.purchase.full_name)

    def test_full_name_is_just_last_name_if_only_has_last_name(self):
        self.PURCHASE_DICT['user_info[first_name]'][0] = ''
        self.assertEqual('Holtslander', self.purchase.full_name)

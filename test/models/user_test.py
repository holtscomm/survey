"""
Tests for User model
"""
from app.models.user import User
from test.fixtures.appengine import GaeTestCase


class UserTests(GaeTestCase):
    def test_create_returns_new_User_entity(self):
        user = User.create()
        self.assertIsInstance(user, User)

    def test_create_takes_first_name_for_user(self):
        user = User.create(first_name='Graham')
        self.assertEqual('Graham', user.first_name)

    def test_create_takes_last_name_for_user(self):
        user = User.create(last_name='Holtslander')
        self.assertEqual('Holtslander', user.last_name)

    def test_create_takes_email_for_user(self):
        user = User.create(email='something@gmail.com')
        self.assertEqual('something@gmail.com', user.email)

    def test_create_set_paid_status_to_False_if_not_passed_in(self):
        user = User.create()
        self.assertEqual(False, user.paid)

    def test_create_takes_paid_status_for_user(self):
        user = User.create(paid=True)
        self.assertEqual(True, user.paid)

    def test_create_assigns_randomized_user_id(self):
        user = User.create()
        self.assertIsInstance(user.user_id, int)

    def test_create_uses_user_id_passed_in(self):
        user = User.create(user_id=1234)
        self.assertEqual(1234, user.user_id)
        actual = User.get_by_user_id(1234)
        self.assertIsNotNone(actual)

    def test_get_user_by_id_returns_correct_user(self):
        expected = User.create(first_name='Graham', last_name='Holtslander')
        user_id = expected.user_id
        actual = User.get_by_user_id(user_id)
        self.assertEqual(expected.first_name, actual.first_name)
        self.assertEqual(expected.last_name, actual.last_name)

    def test_get_or_create_user_by_id_returns_user_if_it_exists(self):
        user = User.create(first_name='Graham', last_name='Holtslander')
        retrieved = User.get_or_create_by_user_id(user.user_id)
        self.assertIsNotNone(retrieved)

    def test_get_or_create_user_by_id_creates_user_if_user_does_not_exist(self):
        retrieved = User.get_or_create_by_user_id(123456)
        self.assertEqual(123456, retrieved.user_id)

    def test_get_or_create_user_by_id_coerces_user_id_to_an_int(self):
        user = User.create(user_id=1234, first_name='Graham')
        actual = User.get_or_create_by_user_id('1234')
        self.assertIsNotNone(actual)
        self.assertEqual(user.first_name, actual.first_name)

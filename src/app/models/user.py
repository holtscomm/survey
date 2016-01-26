"""
User model
"""
import uuid

from google.appengine.ext import ndb


class User(ndb.Model):
    """
    Describes a user of the system.
    """
    user_id = ndb.IntegerProperty(required=True)
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    paid = ndb.BooleanProperty(default=False)

    @classmethod
    def build_key(cls, user_id):
        """
        Build a key for a User entity.
        :param user_id:
        :return:
        """
        return ndb.Key(cls, user_id)

    @classmethod
    def create(cls, first_name=None, last_name=None, email=None, paid=False, user_id=None):
        """
        Create a new user.
        :param first_name:
        :param last_name:
        :param email:
        :param paid:
        :param user_id:
        :return:
        """
        user_id = user_id or int(uuid.uuid4().int % 100000000)
        user = User(
            key=cls.build_key(user_id),
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            paid=paid
        )
        user.put()
        return user

    @classmethod
    def get_by_user_id(cls, user_id):
        """
        Get a user by user id.
        :param user_id:
        :return:
        """
        return cls.build_key(user_id).get()

    @classmethod
    def get_or_create_by_user_id(cls, user_id):
        """
        Get a user by user id if it exists, otherwise create it and return it.
        :param user_id:
        :return:
        """
        if not isinstance(user_id, int):
            user_id = int(user_id)
        user = cls.get_by_user_id(user_id)

        if not user:
            user = cls.create(user_id)

        return user

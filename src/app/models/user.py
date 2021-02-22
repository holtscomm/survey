"""
User model
"""
import uuid

from google.cloud import ndb


class User(ndb.Model):
    """
    Describes a user of the system.
    """
    user_id = ndb.StringProperty(required=True)
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    paid = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)

    @staticmethod
    def _generate_user_id():
        """
        Generate a new user id.
        :return:
        """
        return 'USR-' + uuid.uuid4().hex.upper()

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
        user_id = user_id or cls._generate_user_id()
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

    @property
    def full_name(self):
        """
        Calculates and returns the full name of a User.
        :return: "First Last" or "First" or "Last"
        """
        if self.first_name != '' and self.last_name == '':
            return self.first_name
        elif self.first_name == '' and self.last_name != '':
            return self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    @classmethod
    def get_by_user_id(cls, user_id):
        """
        Get a user by user id.
        :param user_id:
        :return:
        """
        return cls.get_by_user_id_async(user_id).get_result()

    @classmethod
    @ndb.tasklet
    def get_by_user_id_async(cls, user_id):
        """
        Get a user by user id, asynchronously.
        :param user_id:
        :return:
        """
        user = yield cls.build_key(user_id).get_async()
        raise ndb.Return(user)

    @classmethod
    def get_or_create_by_user_id(cls, user_id):
        """
        Get a user by user id if it exists, otherwise create it and return it.
        :param user_id:
        :return:
        """
        if not user_id:
            user_id = cls._generate_user_id()
        user = cls.get_by_user_id(user_id)

        if not user:
            user = cls.create(user_id=user_id)

        return user

    @classmethod
    def get_paid_survey_users(cls):
        """ Get paid survey users """
        return cls.query(cls.paid == True)

    @classmethod
    def get_paid_survey_users_last_30_days(cls):
        """ Get paid survey users in the last 30 days (still todo, just for superadmin stats) """
        return cls.get_paid_survey_users().filter()

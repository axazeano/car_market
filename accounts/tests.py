from django.contrib.auth.models import User
from django.test import TestCase
from .models import Account, AccountsType


class TestAccounts(TestCase):
    def setUp(self):
        # Create test user
        self.user_username = 'TestUser'
        self.user = User(username=self.user_username)
        self.user.save()

        # Create char types
        self.first_type = 'C'
        self.second_type = 'D'

    def test_create_two_accounts_for_user(self):
        """Create two accounts for one user"""
        self.first_account_type = AccountsType(type=self.first_type)
        self.first_account_type.save()
        self.second_account_type = AccountsType(type=self.second_type)
        self.second_account_type.save()

        self.first_account = Account(user=self.user,
                                     type=AccountsType.objects.get(pk=self.first_type), balance=100)
        self.second_account = Account(user=self.user,
                                      type=AccountsType.objects.get(pk=self.second_type), balance=100)
import random
import string
from unittest import TestCase

from accounts.api_v1_admin.serializers import AccountsAdminaccountsRoleSerializer, AccountsAdminUserSerializer
from accounts.models import accountsRole


# <editor-fold desc="serializer unit testing">
class AccountsAdminaccountsRoleSerializerTest(TestCase):
    @staticmethod
    def generate_unique_name():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(10))
        return f"testrole_{random_string}"

    def test_serializer_valid_data(self):
        print("serializer valid test for accounts role")
        role_data = {'name': self.generate_unique_name()}  # Generate unique name
        serializer = AccountsAdminaccountsRoleSerializer(data=role_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        print("serailizer in valid test accounts role")

        role_data = {'name': ''}
        serializer = AccountsAdminaccountsRoleSerializer(data=role_data)
        self.assertFalse(serializer.is_valid())


class AccountsAdminUserSerializerTest(TestCase):
    @staticmethod
    def generate_unique_name():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(10))
        return f"testrole_{random_string}"

    def test_serializer_valid_data(self):
        print("Serializer valid test for accounts user")
        unique_role_name = self.generate_unique_name()
        role = accountsRole.objects.create(name=unique_role_name)
        user_data = {'username': 'testuser', 'role': role.id, 'password': 'testpassword'}
        serializer = AccountsAdminUserSerializer(data=user_data)
        serializer.is_valid()
        self.assertFalse(serializer.errors)

    def test_serializer_invalid_data(self):
        print("Serializer invalid test for accounts user")

        user_data = {'username': ''}
        serializer = AccountsAdminUserSerializer(data=user_data)
        serializer.is_valid()
        self.assertTrue(serializer.errors)
# </editor-fold>

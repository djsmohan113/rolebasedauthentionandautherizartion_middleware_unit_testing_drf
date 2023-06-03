from django.test import TestCase
from django.utils.text import slugify
from accounts.models import accountsRole, User


class AccountsRoleModelTestCase(TestCase):
    def setUp(self):
        self.role = accountsRole.objects.create(name='Test Role')

    def tearDown(self):
        if self.role.id is not None:
            self.role.delete()

    def test_role_create(self):
        print("Testing Role Creation...")
        self.assertEqual(self.role.name, 'Test Role')
        self.assertIsNotNone(self.role.created_at)
        self.assertIsNotNone(self.role.updated_at)
        self.assertIsNotNone(self.role.slug)
        print("Role Created Successfully.")

    def test_role_read(self):
        print("Testing Role Reading...")
        fetched_role = accountsRole.objects.get(id=self.role.id)
        self.assertEqual(fetched_role.name, self.role.name)
        print("Role Read Successfully.")

    def test_role_update(self):
        print("Testing Role Update...")
        new_name = 'Updated Role'
        self.role.name = new_name
        self.role.save()

        updated_role = accountsRole.objects.get(id=self.role.id)
        self.assertEqual(updated_role.name, new_name)
        print("Role Updated Successfully.")

    def test_role_delete(self):
        print("Testing Role Deletion...")
        self.role.delete()
        self.assertFalse(accountsRole.objects.filter(id=self.role.id).exists())
        print("Role Deleted Successfully.")


class UserModelTestCase(TestCase):
    def setUp(self):
        self.role = accountsRole.objects.create(name='Test Role')
        self.user = User.objects.create(username='test_user', role=self.role)

    def tearDown(self):
        if self.user.id is not None:
            self.user.delete()
        if self.role.id is not None:
            self.role.delete()

    def test_user_create(self):
        print("Testing User Creation...")
        self.assertEqual(self.user.username, 'test_user')
        self.assertEqual(self.user.role, self.role)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)
        print("User Created Successfully.")

    def test_user_read(self):
        print("Testing User Reading...")
        fetched_user = User.objects.get(id=self.user.id)
        self.assertEqual(fetched_user.username, self.user.username)
        print("User Read Successfully.")

    def test_user_update(self):
        print("Testing User Update...")
        new_username = 'updated_user'
        self.user.username = new_username
        self.user.save()

        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.username, new_username)
        print("User Updated Successfully.")

    def test_user_delete(self):
        print("Testing User Deletion...")
        user_id = self.user.id
        self.user.delete()
        user_exists = User.objects.filter(id=user_id).exists()
        self.assertFalse(user_exists)
        print("User Deleted Successfully.")












# ==========================================================================
# from unittest import TestCase
#
# from accounts.models import accountsRole, User
#
#
# # <editor-fold desc="models unit testing">
# class AccountsRoleModelTestCase(TestCase):
#     """
#     The purpose of the setUp method is to set up any necessary preconditions or objects that will
#     be used by multiple test cases within the test class.
#     This can include creating database records, initializing objects, or any other setup actions required for the test cases.
#     """
#
#     def setUp(self):
#         self.role = accountsRole.objects.create(name='Test Role')
#
#     def test_role_create(self):
#         """
#         The purpose of assertIsNotNone is to check if a value is not None.
#          If the value is not None, the test case passes.
#         If the value is None, an assertion error is raised, indicating that the test case has failed.
#         """
#         print("Testing Role Creation...")
#         self.assertEqual(self.role.name, 'Test Role')
#         self.assertIsNotNone(self.role.created_at)
#         self.assertIsNotNone(self.role.updated_at)
#         self.assertIsNotNone(self.role.slug)
#         print("Role Created Successfully.")
#
#     def test_role_read(self):
#         """
#         The purpose of assertEqual is to compare two values and assert that they are equal.
#          If the values are equal, the test case passes.
#         If the values are not equal, an assertion error is raised, indicating that the test case has failed.
#         """
#         print("Testing Role Reading...")
#         fetched_role = accountsRole.objects.get(id=self.role.id)
#         self.assertEqual(fetched_role.name, self.role.name)
#         print("Role Read Successfully.")
#
#     def test_role_update(self):
#         print("Testing Role Update...")
#         new_name = 'Updated Role'
#         self.role.name = new_name
#         self.role.save()
#
#         updated_role = accountsRole.objects.get(id=self.role.id)
#         self.assertEqual(updated_role.name, new_name)
#         # self.assertEqual(updated_role.slug, slugify(new_name))
#         print("Role Updated Successfully.")
#
#     def test_role_delete(self):
#         print("Testing Role Deletion...")
#         self.role.delete()
#         self.assertFalse(accountsRole.objects.filter(id=self.role.id).exists())
#         print("Role Deleted Successfully.")
#
#
# class UserModelTestCase(TestCase):
#     def setUp(self):
#         self.role = accountsRole.objects.create(name='Test Role')
#         self.user = User.objects.create(username='test_user', role=self.role)
#
#     def test_user_create(self):
#         print("Testing User Creation...")
#         self.assertEqual(self.user.username, 'test_user')
#         self.assertEqual(self.user.role, self.role)
#         self.assertIsNotNone(self.user.created_at)
#         self.assertIsNotNone(self.user.updated_at)
#         self.assertIsNotNone(self.role.slug)
#         print("User Created Successfully.")
#
#     def test_user_read(self):
#         print("Testing User Reading...")
#         fetched_user = User.objects.get(id=self.user.id)
#         self.assertEqual(fetched_user.username, self.user.username)
#         print("User Read Successfully.")
#
#     def test_user_update(self):
#         print("Testing User Update...")
#         new_username = 'updated_user'
#         self.user.username = new_username
#         self.user.save()
#
#         updated_user = User.objects.get(id=self.user.id)
#         self.assertEqual(updated_user.username, new_username)
#         print("User Updated Successfully.")
#
#     def test_user_delete(self):
#         user_id = self.user.id
#         self.user.delete()
#         user_exists = User.objects.filter(id=user_id).exists()
#         self.assertFalse(user_exists)
#         print("User Deleted Successfully.")
#
# # </editor-fold>

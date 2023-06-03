# from django.test import TestCase
# from accounts.models import accountsRole, User
# from accounts.api_v1_admin.serializers import AccountsAdminaccountsRoleSerializer, AccountsAdminUserSerializer
#
#
# class AccountsAdminaccountsRoleSerializerTest(TestCase):
#     def test_serializer_valid_data(self):
#         print("serailizer valid test accounts role")
#         role_data = {'name': 'Test Role'}
#         serializer = AccountsAdminaccountsRoleSerializer(data=role_data)
#         self.assertTrue(serializer.is_valid())
#
#     def test_serializer_invalid_data(self):
#         print("serailizer in valid test accounts role")
#
#         role_data = {'name': ''}
#         serializer = AccountsAdminaccountsRoleSerializer(data=role_data)
#         self.assertFalse(serializer.is_valid())
#
#
# class AccountsAdminUserSerializerTest(TestCase):
#     def test_serializer_valid_data(self):
#         print("serailizer valid test accounts user")
#         role = accountsRole.objects.create(name='Test Role')
#         user_data = {'username': 'testuser', 'role': role.id}
#         serializer = AccountsAdminUserSerializer(data=user_data)
#         self.assertTrue(serializer.is_valid())
#
#     def test_serializer_invalid_data(self):
#         print("serailizer invalid test accounts  user")
#
#         user_data = {'username': ''}
#         serializer = AccountsAdminUserSerializer(data=user_data)
#         self.assertFalse(serializer.is_valid())
#
#
#
#
#
#
#
#
#
#
#
# # url testing
# # class accountsAdminAccountsRoleEndpointAPITestCase(APITestCase):
# #     def setUp(self):
# #         self.client = APIClient()
# #
# #     def test_get_all_accounts_roles(self):
# #         print("get all accounts roles list")
# #         url = reverse("accountsAdminAccountRoleCreateGenericsViewURL")
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         # Add additional assertions to validate the response data or structure
# #         # Example: self.assertEqual(len(response.data), expected_count_of_accounts_roles)
# #
# #     #
# #     def test_create_accounts_role(self):
# #         print("accounts role created")
# #         url = reverse("accountsAdminAccountRoleCreateGenericsViewURL")
# #         data = {
# #             # Provide the necessary data for creating an accounts role
# #             # Example: "name": "Admin"
# #             "name": "Admin"
# #         }
# #         response = self.client.post(url, data)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data["message"], "account role Created successfully")
# #
# #     def test_get_accounts_role_details(self):
# #         print("accounts role get by id ")
# #         accounts_role = accountsRole.objects.create(name="Admin")
# #         url = reverse("accountsAdminAccountsRoleDetailsAPIViewURL", args=[accounts_role.id])
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data["name"], "Admin")
# #
# #     def test_update_accounts_role(self):
# #         print("update accounts role by id")
# #         accounts_role = accountsRole.objects.create(name="Admin")
# #         url = reverse("accountsAdminAccountsRoleDetailsAPIViewURL", args=[accounts_role.id])
# #         data = {
# #             # Provide the necessary data for updating the accounts role
# #             # Example: "name": "Super Admin"
# #             "name": "Super Admin"
# #         }
# #         response = self.client.put(url, data)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data["name"], "Super Admin")
# #
# #     #
# #     def test_delete_accounts_role(self):
# #         print("accounts role delete by id ")
# #         accounts_role = accountsRole.objects.create(name="Admin")
# #         url = reverse("accountsAdminAccountsRoleDetailsAPIViewURL", args=[accounts_role.id])
# #         response = self.client.delete(url)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data["data"], "Objects Deleted Successfully")
# #
# # class accountsAdminUserEndpointAPITestCase(APITestCase):
# #     def setUp(self):
# #         self.client = APIClient()
# #
# #     def test_get_all_users(self):
# #         print("accounts user get all ")
# #         User.objects.create_user(username="user1", password="password123", email="user1@example.com")
# #         User.objects.create_user(username="user2", password="password456", email="user2@example.com")
# #
# #         url = reverse("accountsAdminAccountUserCreateGenericsViewURL")
# #         response = self.client.get(url)
# #
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         # self.assertEqual(len(response.data), 2)
# #
# #
# #     def test_create_user(self):
# #         print("now user create test")
# #         url = reverse("accountsAdminAccountUserCreateGenericsViewURL")
# #         data = {
# #             # Provide the necessary data for creating a user
# #             # Example: "username": "testuser", "password": "password123", "email": "test@example.com"
# #             "username": "testuser", "password": "password123", "email": "test@example.com"
# #         }
# #         response = self.client.post(url, data)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data["message"],"account user Created successfully")
# #
# #         # self.assertTrue(User.objects.filter(username="user1").exists())
# #         # self.assertTrue(User.objects.filter(username="user2").exists())
# #
# #
# #     def test_get_user_details(self):
# #         print("accounts user details get by id")
# #         user = User.objects.create_user(username="testuser", password="password123", email="test@example.com")
# #         url = reverse("accountsAdminAccountsUserDetailsAPIViewURL", args=[user.id])
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data["username"], "testuser")
# #
# #     def test_update_user(self):
# #         print("accounts user update by id")
# #         user = User.objects.create_user(username="testuser", password="password123", email="test@example.com")
# #         url = reverse("accountsAdminAccountsUserDetailsAPIViewURL", args=[user.id])
# #         data = {
# #             # Provide the necessary data for updating the user
# #             # Example: "email": "new@example.com"
# #             "email": "new@example.com"
# #         }
# #         response = self.client.put(url, data)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data["email"], "new@example.com")
# #
# #     def test_delete_user(self):
# #         print("accounts user delete now")
# #         user = User.objects.create_user(username="testuser", password="password123", email="test@example.com")
# #         url = reverse("accountsAdminAccountsUserDetailsAPIViewURL", args=[user.id])
# #         response = self.client.delete(url)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #         self.assertEqual(response.data["data"], "Objects Deleted Successfully")

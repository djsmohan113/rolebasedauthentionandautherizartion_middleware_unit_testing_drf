from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.test import RequestFactory

from accounts.api_v1_admin.views import accountsAdminAccountUserCreateGenericsView, accountsAdminAccountsUserDetailsAPIView
from accounts.models import User, accountsRole
from rest_framework.test import APIClient


# <editor-fold desc="authentication with views unit testing">
class AccountsAdminAccountRoleCreateGenericsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.view_url = reverse('accountsAdminAccountRoleCreateGenericsViewURL')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

    def test_get_request_with_authentication(self):
        print("GET request for account role view with authentication")
        self.client.force_login(self.user)

        response = self.client.get(self.view_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_request_without_authentication(self):
        print("GET request for account role view without authentication")
        self.client.logout()

        response = self.client.get(self.view_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_request_with_authentication(self):
        print("POST request for account role with authentication")
        self.client.force_login(self.user)

        role_data = {'name': 'Test Role'}
        response = self.client.post(self.view_url, data=role_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'account role Created successfully')

    def test_post_request_without_authentication(self):
        print("POST request for account role without authentication")
        self.client.logout()

        role_data = {'name': 'Test Role'}
        response = self.client.post(self.view_url, data=role_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AccountsAdminAccountsRoleDetailsAPIViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.role = accountsRole.objects.create(name='Test Role')
        self.view_url = reverse('accountsAdminAccountsRoleDetailsAPIViewURL', args=[self.role.id])

    def test_get_request_with_authentication(self):
        print("Account role get by id with authentication")
        token = 'Token ' + self.token.key

        response = self.client.get(self.view_url, HTTP_AUTHORIZATION=token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_request_without_authentication(self):
        print("Account role get by id without authentication")
        response = self.client.get(self.view_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_request_with_authentication(self):
        print("Account role put request by id with authentication")
        token = 'Token ' + self.token.key

        role_data = {'name': 'Updated Role'}
        response = self.client.put(
            self.view_url,
            data=role_data,
            content_type='application/json',
            HTTP_AUTHORIZATION=token
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Role')

    def test_put_request_without_authentication(self):
        print("Account role put request by id without authentication")
        role_data = {'name': 'Updated Role'}
        response = self.client.put(
            self.view_url,
            data=role_data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_request_with_authentication(self):
        print("Account role delete request by id with authentication")
        token = 'Token ' + self.token.key

        response = self.client.delete(
            self.view_url,
            content_type='application/json',
            HTTP_AUTHORIZATION=token
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], 'Objects Deleted Successfully')

    def test_delete_request_without_authentication(self):
        print("Account role delete request by id without authentication")
        response = self.client.delete(
            self.view_url,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class AccountsAdminAccountUserCreateGenericsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = accountsAdminAccountUserCreateGenericsView.as_view()
        self.url = reverse('accountsAdminAccountUserCreateGenericsViewURL')

    def test_get_request_without_authentication(self):
        print("Get all request view account user without authentication")
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 401)

    def test_get_request_with_authentication(self):
        print("Get all request view account user with authentication")
        user = User.objects.create(username='testuser')
        token = Token.objects.create(user=user)

        request = self.factory.get(self.url, HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_post_request_with_authentication(self):
        print("account user post request with authentication")
        user = User.objects.create(username='testuser1', password='testpassword')
        token = Token.objects.create(user=user)

        client = APIClient()
        client.force_authenticate(user=user)

        role = accountsRole.objects.create(name='Test Role')
        user_data = {
            'username': 'testuser2',
            'password': 'testpassword',
            'role': role.id,
        }
        response = client.post(self.url, data=user_data)
        if response.status_code == 400:
            print(response.data)  # Print the serializer errors
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'User created successfully')
    def test_post_request_without_authentication(self):
        print("account user post request without authentication")
        role = accountsRole.objects.create(name='Test Role')
        user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'role': role.id,
        }
        response = self.client.post(self.url, data=user_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class AccountsAdminAccountsUserDetailsAPIViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = accountsAdminAccountsUserDetailsAPIView.as_view()
        self.role = accountsRole.objects.create(name='Test Role')
        self.user = User.objects.create(username='testuser', role=self.role)
        self.url = reverse('accountsAdminAccountsUserDetailsAPIViewURL', args=[self.user.id])

    def test_get_request_without_authentication(self):
        print("Account User get by id without authentication")
        request = self.factory.get(self.url)
        response = self.view(request, id=self.user.id)
        self.assertEqual(response.status_code, 401)

    def test_get_request_with_authentication(self):
        print("Account User get by id with authentication")
        user = User.objects.create(username='testuser3')
        token = Token.objects.create(user=user)

        request = self.factory.get(self.url, HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.view(request, id=self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_put_request_without_authentication(self):
        print("Account user put request by id without authentication")
        role = accountsRole.objects.create(name='Updated Role')
        user_data = {
            'username': 'updateduser',
            'role': role.id
        }
        request = self.factory.put(self.url, data=user_data, content_type='application/json')
        response = self.view(request, id=self.user.id)
        self.assertEqual(response.status_code, 401)

    def test_put_request_with_authentication(self):
        print("Account user put request by id with authentication")
        role = accountsRole.objects.create(name='Updated Role')
        user_data = {
            'username': 'updateduser',
            'role': role.id
        }

        user = User.objects.create(username='testuser4')
        token = Token.objects.create(user=user)

        request = self.factory.put(
            self.url,
            data=user_data,
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + token.key
        )
        response = self.view(request, id=self.user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'updateduser')

    def test_delete_request_without_authentication(self):
        print("Account user delete request by id without authentication")
        request = self.factory.delete(self.url, content_type='application/json')
        response = self.view(request, id=self.user.id)
        self.assertEqual(response.status_code, 401)

    def test_delete_request_with_authentication(self):
        print("Account user delete request by id with authentication")
        user = User.objects.create(username='testuser5')
        token = Token.objects.create(user=user)

        request = self.factory.delete(
            self.url,
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + token.key
        )
        response = self.view(request, id=self.user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], 'Objects Deleted Successfully')
# </editor-fold>















# ==============without auth===============================

# from django.test import RequestFactory
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
#
# from accounts.api_v1_admin.views import accountsAdminAccountRoleCreateGenericsView, accountsAdminAccountsRoleDetailsAPIView, accountsAdminAccountsUserDetailsAPIView, accountsAdminAccountUserCreateGenericsView
# from accounts.models import accountsRole, User
#
#
# # <editor-fold desc="views unit testing">
# class AccountsAdminAccountRoleCreateGenericsViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.view = accountsAdminAccountRoleCreateGenericsView.as_view()
#         self.url = reverse('accountsAdminAccountRoleCreateGenericsViewURL')
#
#     def test_get_request(self):
#         print("get all request view account role")
#         request = self.factory.get(self.url)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200)
#
#     def test_post_request(self):
#         print("post request account role")
#         role_data = {'name': 'Test Role'}
#         request = self.factory.post(self.url, data=role_data)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['message'], 'account role Created successfully')
#
#
# class AccountsAdminAccountsRoleDetailsAPIViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.view = accountsAdminAccountsRoleDetailsAPIView.as_view()
#         self.role = accountsRole.objects.create(name='Test Role')
#         self.url = reverse('accountsAdminAccountsRoleDetailsAPIViewURL', args=[self.role.id])
#
#     def test_get_request(self):
#         print("account role get by id ")
#         request = self.factory.get(self.url)
#         response = self.view(request, id=self.role.id)
#         self.assertEqual(response.status_code, 200)
#
#     def test_put_request(self):
#         print("account role put request by id")
#         role_data = {'name': 'Updated Role'}
#         request = self.factory.put(self.url, data=role_data, content_type='application/json')
#         response = self.view(request, id=self.role.id)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], 'Updated Role')
#
#     def test_delete_request(self):
#         print("account role delete request by id")
#         request = self.factory.delete(self.url, content_type='application/json')
#         response = self.view(request, id=self.role.id)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['data'], 'Objects Deleted Successfully')

#
# class AccountsAdminAccountUserCreateGenericsViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.view = accountsAdminAccountUserCreateGenericsView.as_view()
#         self.url = reverse('accountsAdminAccountUserCreateGenericsViewURL')
#
#     def test_get_request(self):
#         print("get all request view account user")
#         request = self.factory.get(self.url)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200)
#
#     def test_post_request(self):
#         print(" account user post request")
#         role = accountsRole.objects.create(name='Test Role')
#         user_data = {
#             'username': 'testuser',
#             'password': 'testpassword',
#             'role': role.id,
#         }
#         request = self.factory.post(self.url, data=user_data)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['message'], 'User created successfully')
#
#
# class AccountsAdminAccountsUserDetailsAPIViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.view = accountsAdminAccountsUserDetailsAPIView.as_view()
#         self.role = accountsRole.objects.create(name='Test Role')
#         self.user = User.objects.create(username='testuser', role=self.role)
#         self.url = reverse('accountsAdminAccountsUserDetailsAPIViewURL', args=[self.user.id])
#
#     def test_get_request(self):
#         print(" account User get by id")
#         request = self.factory.get(self.url)
#         response = self.view(request, id=self.user.id)
#         self.assertEqual(response.status_code, 200)
#
#     def test_put_request(self):
#         print(" account user put request by id")
#         role = accountsRole.objects.create(name='Updated Role')
#         user_data = {
#             'username': 'updateduser',
#             'role': role.id
#         }
#         request = self.factory.put(self.url, data=user_data, content_type='application/json')
#         response = self.view(request, id=self.user.id)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['username'], 'updateduser')
#
#     def test_delete_request(self):
#         print("account user delete request by id")
#         request = self.factory.delete(self.url, content_type='application/json')
#         response = self.view(request, id=self.user.id)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['data'], 'Objects Deleted Successfully')
#

# # # </editor-fold>

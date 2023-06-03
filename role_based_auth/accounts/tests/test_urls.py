from audioop import reverse

from django.test import TestCase
from django.urls import reverse, resolve

from accounts.api_v1_admin.views import accountsAdminAccountRoleCreateGenericsView, accountsAdminAccountsRoleDetailsAPIView, accountsAdminAccountUserCreateGenericsView, accountsAdminAccountsUserDetailsAPIView


# <editor-fold desc="url unit testing ">


class AccountsURLsTest(TestCase):
    def test_accounts_role_create_url(self):
        url = reverse('accountsAdminAccountRoleCreateGenericsViewURL')
        print("URL:", url)
        resolver = resolve(url)
        print("Resolved View:", resolver.func.__name__)
        self.assertEqual(
            resolver.func.__name__,
            accountsAdminAccountRoleCreateGenericsView.as_view().__name__,
        )

    def test_accounts_role_details_url(self):
        url = reverse('accountsAdminAccountsRoleDetailsAPIViewURL', args=[1])  # Replace 1 with a valid ID
        print("URL:", url)
        resolver = resolve(url)
        print("Resolved View:", resolver.func.__name__)
        self.assertEqual(
            resolver.func.__name__,
            accountsAdminAccountsRoleDetailsAPIView.as_view().__name__,
        )

    def test_accounts_user_create_url(self):
        url = reverse('accountsAdminAccountUserCreateGenericsViewURL')
        print("URL:", url)
        resolver = resolve(url)
        print("Resolved View:", resolver.func.__name__)
        self.assertEqual(
            resolver.func.__name__,
            accountsAdminAccountUserCreateGenericsView.as_view().__name__,
        )

    def test_accounts_user_details_url(self):
        url = reverse('accountsAdminAccountsUserDetailsAPIViewURL', args=[1])  # Replace 1 with a valid ID
        print("URL:", url)
        resolver = resolve(url)
        print("Resolved View:", resolver.func.__name__)
        self.assertEqual(
            resolver.func.__name__,
            accountsAdminAccountsUserDetailsAPIView.as_view().__name__,
        )
# </editor-fold>


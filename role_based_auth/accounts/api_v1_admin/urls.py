from django.urls import path

from .views import *

urlpatterns = [


    # <editor-fold desc="Api For accounts role get,post">
    path('accounts_role_main/',accountsAdminAccountRoleCreateGenericsView.as_view(),name="accountsAdminAccountRoleCreateGenericsViewURL"),
    # </editor-fold>

    # <editor-fold desc="Api for accounts role get,put,delete">
    path('accounts_role_main/<id>/',accountsAdminAccountsRoleDetailsAPIView.as_view(),name="accountsAdminAccountsRoleDetailsAPIViewURL"),
    # </editor-fold>

    # <editor-fold desc="Api For accounts user get,post">
    path('accounts_user_main/',accountsAdminAccountUserCreateGenericsView.as_view(),name="accountsAdminAccountUserCreateGenericsViewURL"),
    # </editor-fold>

    # <editor-fold desc="Api for accounts user get,put,delete">
    path('accounts_user_main/<id>/',accountsAdminAccountsUserDetailsAPIView.as_view(),name="accountsAdminAccountsUserDetailsAPIViewURL"),
    # </editor-fold>



]

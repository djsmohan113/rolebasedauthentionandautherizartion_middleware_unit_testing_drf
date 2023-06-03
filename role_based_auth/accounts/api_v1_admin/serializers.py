from rest_framework import serializers
from accounts.models import accountsRole, User

class AccountsAdminaccountsRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountsRole
        fields = '__all__'

class AccountsAdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

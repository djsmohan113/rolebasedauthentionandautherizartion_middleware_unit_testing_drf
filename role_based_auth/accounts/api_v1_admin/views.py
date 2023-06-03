from rest_framework import generics
# import django_filters
# from django_filters import rest_framework as dj_filter
from rest_framework import generics, filters, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import accountsRole, User
from .serializers import *

# <editor-fold desc="View For account role Get and Post">
class accountsAdminAccountRoleCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = AccountsAdminaccountsRoleSerializer
    queryset = accountsRole.objects.all()
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = LimitOffsetPagination
    search_fields = ["name", ]
    # filter_backends = (filters.SearchFilter, dj_filter.DjangoFilterBackend, filters.OrderingFilter,)
    # filterset_class = shippingsAdminShippingFilter

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = AccountsAdminaccountsRoleSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "account role Created successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>


# <editor-fold desc="View For accounts role get,put ,delete">
class accountsAdminAccountsRoleDetailsAPIView(APIView):
    serializer_class = AccountsAdminaccountsRoleSerializer
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = None

    def get(self, request, id):
        try:
            data = accountsRole.objects.get(id=id)
        except:
            return Response({"message": "accounts role Does Not Exist", "status": status.HTTP_400_BAD_REQUEST})

        serializer = AccountsAdminaccountsRoleSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            data = accountsRole.objects.get(id=id)
        except:
            return Response({"message": "accounts role Does Not Exist", "status": status.HTTP_400_BAD_REQUEST})

        serializer = AccountsAdminaccountsRoleSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            data = accountsRole.objects.get(id=id)
        except:
            return Response({"message": "accounts Does Not Exist", "status": status.HTTP_400_BAD_REQUEST})
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_200_OK)
# </editor-fold>


# <editor-fold desc="View For account user Get and Post">
class accountsAdminAccountUserCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = AccountsAdminUserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = LimitOffsetPagination
    search_fields = ["name", ]
    # filter_backends = (filters.SearchFilter, dj_filter.DjangoFilterBackend, filters.OrderingFilter,)
    # filterset_class = shippingsAdminShippingFilter

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = AccountsAdminUserSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>


# <editor-fold desc="View For accounts user get,put ,delete">
class accountsAdminAccountsUserDetailsAPIView(APIView):
    serializer_class = AccountsAdminUserSerializer
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = None

    def get(self, request, id):
        try:
            data = User.objects.get(id=id)
        except:
            return Response({"message": "accounts user Does Not Exist", "status": status.HTTP_400_BAD_REQUEST})

        serializer = AccountsAdminUserSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            data = User.objects.get(id=id)
        except:
            return Response({"message": "accounts user Does Not Exist", "status": status.HTTP_400_BAD_REQUEST})

        serializer = AccountsAdminUserSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            data = User.objects.get(id=id)
        except:
            return Response({"message": "accounts user Not Exist", "status": status.HTTP_400_BAD_REQUEST})
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_200_OK)
# </editor-fold>

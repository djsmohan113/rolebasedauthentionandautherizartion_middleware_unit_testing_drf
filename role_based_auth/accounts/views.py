# views.py
#
# from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
#
# from .models import User
# from accounts.api_v1_admin.serializers import AccountsAdminUserSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = AccountsAdminUserSerializer
#     permission_classes = (IsAuthenticated,)
#     authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#





























# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.urls import reverse
#
# def login_view(request):
#     error_message=None
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             # Log in the user
#             login(request, user)
#
#             # Redirect to a suitable page based on the user's role
#             if user.role.name == 'admin':
#                 return redirect(reverse('admin'))
#             elif user.role.name == 'teacher':
#                 return redirect(reverse('teacher'))
#             elif user.role.name == 'student':
#                 return redirect(reverse('student'))
#         else:
#             # Invalid credentials
#             error_message = 'Invalid username or password.'
#
#     return render(request, 'login.html', {'error_message': error_message})
#
# def logout_view(request):
#     # Log out the user
#     logout(request)
#
#     # Redirect to the login page or any other suitable page
#     return redirect(reverse('login'))
#
# def admin_view(request):
#     # Check if the user is an admin
#     if request.user.role.name != 'admin':
#         return redirect(reverse('forbidden'))
#
#     # Admin view logic here
#
#     return render(request, 'admin.html')
#
# def teacher_view(request):
#     # Check if the user is a teacher
#     if request.user.role.name != 'teacher':
#         return redirect(reverse('forbidden'))
#
#     # Teacher view logic here
#
#     return render(request, 'teacher.html')
#
# def student_view(request):
#     # Check if the user is a student
#     if request.user.role.name != 'student':
#         return redirect(reverse('forbidden'))
#
#     # Student view logic here
#
#     return render(request, 'student.html')
#
# def forbidden_view(request):
#     return render(request, 'forbidden.html')

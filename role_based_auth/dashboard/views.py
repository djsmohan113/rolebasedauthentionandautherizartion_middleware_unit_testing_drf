# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                # Reject superuser login
                return render(request, 'dashboard/login.html', {'error_message': 'Superuser login not allowed.'})

            if hasattr(user, 'role') and user.role is not None and hasattr(user.role, 'name') and user.role.name is not None:
                login(request, user)
                if user.role.name == 'admin':
                    return redirect('admin_dashboard')
                elif user.role.name == 'student':
                    return redirect('student_dashboard')
                elif user.role.name == 'teacher':
                    return redirect('teacher_dashboard')
            else:
                # Handle missing or invalid role
                return render(request, 'dashboard/login.html', {'error_message': 'Invalid user role.'})
        else:
            # Handle invalid login credentials
            return render(request, 'dashboard/login.html', {'error_message': 'Invalid username or password.'})
    else:
        # Render login template
        return render(request, 'dashboard/login.html')


@login_required
@never_cache
def admin_dashboard(request):
    return render(request, 'dashboard/admin.html')


@login_required
@never_cache
def student_dashboard(request):
    return render(request, 'dashboard/student.html')


@login_required
@never_cache
def teacher_dashboard(request):
    return render(request, 'dashboard/teacher.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def error_page(request):
    return render(request, 'dashboard/error.html')

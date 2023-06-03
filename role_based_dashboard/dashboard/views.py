from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                # Reject superuser login
                return render(request, 'login.html', {'error_message': 'Superuser login not allowed.'})

            if hasattr(user, 'role') and user.role is not None and user.role.name is not None:
                login(request, user)
                if user.role.name == 'admin':
                    return redirect('admin_dashboard')
                elif user.role.name == 'student':
                    return redirect('student_dashboard')
                elif user.role.name == 'teacher':
                    return redirect('teacher_dashboard')

            else:
                # Handle missing or invalid role
                return render(request, 'login.html', {'error': 'Invalid user role.'})
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        # Render login template
        return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
@login_required
@never_cache
def admin_dashboard(request):
    return render(request, 'admin.html')

@login_required
@never_cache
def student_dashboard(request):
    return render(request, 'student.html')

@login_required
@never_cache
def teacher_dashboard(request):
    return render(request, 'teacher.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def error_page(request):
    return render(request, 'error.html')

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse
from django.utils.cache import add_never_cache_headers


class RoleMiddleware:
    """
    Middleware class for role-based redirection and authentication in a Django web application.

    This middleware intercepts requests and performs the following actions:
    - Redirects unauthenticated users to the login page, except for the login page itself and restricted pages.
    - Redirects authenticated users to their respective dashboards based on their role.
    - Handles user logout by redirecting to the login page.
    - Adds cache headers to the response to prevent caching.

    Usage:
    Include this middleware in the Django settings.py file's MIDDLEWARE setting.

    Explanation of role-based redirection:
    - The middleware checks if the user is authenticated and has a role assigned.
    - If the user is authenticated and the requested path is not their respective dashboard or the logout page:
        - The middleware determines the user's role by accessing the 'role' attribute of the user object.
        - It uses a dictionary, `role_mappings`, to map roles to their corresponding dashboard URLs.
        - If the user's role is found in the `role_mappings` dictionary, the middleware redirects the user to their respective dashboard URL.
        - If the user's role is not found in the `role_mappings` dictionary, it redirects the user to the 'login' page.
    - If the requested path is the login page and the user is already authenticated with a role:
        - The middleware redirects the user to their respective dashboard based on their role.

    Note:
    - The mapping of roles to dashboard URLs should be defined in the `role_mappings` dictionary.
    - The 'role' attribute of the user object should be set appropriately in your Django application.

    Example `role_mappings` dictionary:
    role_mappings = {
        'admin': 'admin_dashboard',
        'student': 'student_dashboard',
        'teacher': 'teacher_dashboard',
    }
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Debug: RoleMiddleware - __call__ method called.")

        if not request.user.is_authenticated:
            if request.path != '/login/':
                print("Debug: User not authenticated. Redirecting to login page.")
                return HttpResponseRedirect(reverse('login'))
            if request.path in ['/logout/', '/admin_dashboard/', '/student_dashboard/', '/teacher_dashboard/']:
                print("Debug: User not authenticated. Redirecting to login page.")
                return HttpResponseRedirect(reverse('login'))
        else:
            if request.path == '/logout/':
                print("Debug: User logged out. Redirecting to login page.")
                logout(request)
                return HttpResponseRedirect(reverse('login'))

            role_mappings = {
                'admin': 'admin_dashboard',
                'student': 'student_dashboard',
                'teacher': 'teacher_dashboard',
            }
            user_role = request.user.role.name if hasattr(request.user, 'role') else None
            if user_role and request.path not in [f'/{user_role}_dashboard/', '/logout/']:
                print(f"Debug: User role: {user_role}. Redirecting to {role_mappings.get(user_role, 'login')} dashboard.")
                return redirect(role_mappings.get(user_role, 'login'))

            if request.path == '/login/':
                if user_role:
                    print(f"Debug: User already authenticated with role: {user_role}. Redirecting to {role_mappings.get(user_role, 'login')} dashboard.")
                    return redirect(role_mappings.get(user_role, 'login'))

        response = self.get_response(request)
        add_never_cache_headers(response)
        return response

# from django.shortcuts import redirect
# from django.http import HttpResponseRedirect
# from django.contrib.auth import logout
# from django.urls import reverse
#
#
# class RoleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         if not request.user.is_authenticated:
#             if request.path != '/login/':
#                 print('Redirecting to login')
#                 return HttpResponseRedirect(reverse('login'))
#             # Prevent access to dashboard pages for logged-out users
#             if request.path in ['/logout/', '/admin_dashboard/', '/student_dashboard/', '/teacher_dashboard/']:
#                 print('Redirecting to login')
#                 return HttpResponseRedirect(reverse('login'))
#         else:
#             if request.path == '/logout/':
#                 print('Logging out')
#                 logout(request)
#                 return HttpResponseRedirect(reverse('login'))  # Redirect to desired page after logout
#             if hasattr(request.user, 'role'):
#                 if request.user.role.name == 'admin' and request.path not in ['/admin_dashboard/', '/logout/']:
#                     print('Redirecting admin to admin_dashboard')
#                     return redirect('admin_dashboard')
#                 elif request.user.role.name == 'student' and request.path not in ['/student_dashboard/', '/logout/']:
#                     print('Redirecting student to student_dashboard')
#                     return redirect('student_dashboard')
#                 elif request.user.role.name == 'teacher' and request.path not in ['/teacher_dashboard/', '/logout/']:
#                     print('Redirecting teacher to teacher_dashboard')
#                     return redirect('teacher_dashboard')
#
#         if request.path == '/login/':
#             print('Already authenticated, redirecting to dashboard')
#             if hasattr(request.user, 'role'):
#                 if request.user.role.name == 'admin':
#                     return redirect('admin_dashboard')
#                 elif request.user.role.name == 'student':
#                     return redirect('student_dashboard')
#                 elif request.user.role.name == 'teacher':
#                     return redirect('teacher_dashboard')
#
#         response = self.get_response(request)
#         return response

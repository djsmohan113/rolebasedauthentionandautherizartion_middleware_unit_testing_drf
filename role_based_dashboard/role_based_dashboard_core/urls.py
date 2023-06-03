"""role_based_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),















    # path('login/', login, name='login'),
    # path('student/', student_dashboard, name='student_dashboard'),
    # path('teacher/', teacher_dashboard, name='teacher_dashboard'),
    # path('admin/', admin_dashboard, name='admin_dashboard'),
    #











    # path('', views.common_dashboard, name='common_dashboard'),
    # path('student/', views.student_dashboard, name='student_dashboard'),
    # path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    # path('admin/', views.admin_dashboard, name='admin_dashboard'),
    # path('login/', views.login_view, name='login'),
    # path('', index, name='index'),
    # path('login/', login_view, name='login'),
    # path('dashboard/common/', common_dashboard, name='common_dashboard'),
    # path('dashboard/student/', student_dashboard, name='student_dashboard'),
    # path('dashboard/teacher/', teacher_dashboard, name='teacher_dashboard'),
    # path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    # path('logout/', user_logout, name='user_logout'),
]

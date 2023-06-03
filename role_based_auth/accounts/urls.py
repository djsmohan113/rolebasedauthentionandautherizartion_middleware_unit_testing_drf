# urls.py

from django.urls import include, path

urlpatterns = [
    path('api/v1/admin/', include("accounts.api_v1_admin.urls")),

]

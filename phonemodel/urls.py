from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phonemodelapi/', include('phonemodelapi.urls')),
    path('auth/', obtain_auth_token)
]


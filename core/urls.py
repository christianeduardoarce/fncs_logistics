from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('fcns_logistics:dashboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('fcns_logistics.urls')),
    path('', home_redirect, name='home'),
]
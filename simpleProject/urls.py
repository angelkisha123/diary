from django.contrib import admin
from django.http import HttpResponse
from django.urls import path , include

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    
]

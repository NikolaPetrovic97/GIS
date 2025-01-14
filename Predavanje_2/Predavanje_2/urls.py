from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('app/', include('Prvi_sistem.urls')),
    path('admin/', admin.site.urls)
]

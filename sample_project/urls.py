# dummy_certificate/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('certificates/', include('certificates.urls')),
]

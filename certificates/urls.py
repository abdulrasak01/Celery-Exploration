# certificates/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate_certificate/<str:name>/', views.request_certificate, name='generate_certificate'),
]

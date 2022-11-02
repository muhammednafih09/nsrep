from django.urls import path
from . import views

urlpatterns = [
    path('', views.scanner),
    path('scan-form/', views.scan_form, name='scan-form'),
]
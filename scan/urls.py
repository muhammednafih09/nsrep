from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_json_table_format),
    path('scan-form/', views.scan_form, name='scan-form'),
]
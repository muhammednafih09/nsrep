from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('add-user/', views.addUser, name="add-user"),
    path('view-user/', views.viewUser, name="view-user"),   
    path('profile/', views.profile, name="profile"), 
    path('my-scans/', views.myScans, name="my-scans"),
    path('all-scans/', views.allScans, name="all-scans"),
    path('reports/', views.reports, name="reports"),
    path('info/', views.info, name="info"),
    path('', views.loggedIn, name="dashboard"),   
]
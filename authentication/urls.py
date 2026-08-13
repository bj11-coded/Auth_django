"""
URL configuration for authentication project.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logins , name ="login"),
    path('register/', views.register, name ="register"),
    path('forgotpassword/', views.forgotpassword, name ="forgotpassword"),
    path('dashboard/', views.dashboard, name ="dashboard")
]

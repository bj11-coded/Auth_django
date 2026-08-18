"""
URL configuration for authentication project.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logins , name ="login"),
    path('register/', views.register, name ="register"),
    path('forgotpassword/', views.forgotpassword, name ="forgotpassword"),
    path('dashboard/', views.dashboard, name ="dashboard"),

    #api 
    path('product/',views.products, name="product_list"),

    #frontend
    path('productpage/', views.product_page, name="product_page")
]

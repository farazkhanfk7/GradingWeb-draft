from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register', views.register, name="register"),
    path('upload', views.upload, name="upload"),
    path('contact',views.contact,name="contact")
]

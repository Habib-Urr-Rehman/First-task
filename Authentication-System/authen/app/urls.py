from django.contrib import admin
from django.urls import path,include
from .views import*
urlpatterns = [
    path('',user_signup),
    path('signup/',user_signup),
    path('login/',user_login),
    path("home/",home_page)
]
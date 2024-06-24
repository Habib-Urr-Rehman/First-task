from django.contrib import admin
from django.urls import path,include
from .views import*
urlpatterns = [
    path('',signup),
    path('signup/',signup),
    path('login/',userlogin),
    path("home/",homepage)
    
    
     
]
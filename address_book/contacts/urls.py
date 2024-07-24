from django.urls import path
from .views import contact_list, add_contact

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('add/', add_contact, name='add_contact'),
]


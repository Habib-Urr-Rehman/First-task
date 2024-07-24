# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'contact_number', 'years_of_experience', 'university_name', 'degree_name', 'is_staff')
    list_editable = ('contact_number', 'years_of_experience', 'university_name', 'degree_name')

# Register CustomUser with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)


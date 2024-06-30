from django.contrib import admin
from contacts.models import Contact
# Register your models here.

class AddressBook(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone_number','address')
   
admin.site.register(Contact,AddressBook)
#





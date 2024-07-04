from django.contrib import admin
from api.models import *

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['company_id','name','location','about','type','added_date','active']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','email','address','phone','about','postion','company']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)

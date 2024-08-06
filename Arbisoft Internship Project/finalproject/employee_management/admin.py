from django.contrib import admin
from employee_management.models import *
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['company_id','name','location','about','type','added_date','active']

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['department_id','name','company']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'name','description', 'start_date', 'end_date', 'company']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Project,ProjectAdmin)


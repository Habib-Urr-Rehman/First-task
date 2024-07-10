from django.contrib import admin
from apiviews.models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display=['company_id','name','location','about','type','added_date','active']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'phone', 'about', 'postion', 'company', 'department']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'name','description', 'start_date', 'end_date', 'company','display_employees']
    def display_employees(self, obj):
        return ", ".join([employee.name for employee in obj.employees.all()])
    display_employees.short_description = 'Employees'

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['department_id','name','company']

class HrDepartmentAdmin(admin.ModelAdmin):
    list_display=['hr_name','department_id','name','company']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(HrDepartment,HrDepartmentAdmin)


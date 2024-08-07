from django.contrib import admin
from employee_management.models import *
from employee_management.models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CompanyAdmin(admin.ModelAdmin):
    list_display=['company_id','name','location','about','type','added_date','active']

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['department_id','name','company']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'name','description', 'start_date', 'end_date', 'company']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'phone', 'about', 'position', 'company', 'department','user']

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role','is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

class ReimbursementAdmin(admin.ModelAdmin):
    list_display = ('employee', 'type', 'amount', 'date', 'status')

class LeaveManagementAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'is_approved')

class TimeTrackingAdmin(admin.ModelAdmin):
    list_display = ['employee', 'project', 'date']

class DailyTimeLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_employee', 'get_project', 'get_date', 'hours', 'task_type', 'description']
    
    def get_employee(self, obj):
        return obj.time_tracking.employee
    
    def get_project(self, obj):
        return obj.time_tracking.project

    def get_date(self, obj):
        return obj.time_tracking.date
    
    get_employee.short_description = 'Employee'
    get_project.short_description = 'Project'
    get_date.short_description = 'Date'

class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ['employee', 'review_date', 'performance_score', 'comments']
 
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    
admin.site.register(Training,TrainingAdmin)
admin.site.register(PerformanceReview,PerformanceReviewAdmin)
admin.site.register(TimeTracking,TimeTrackingAdmin)
admin.site.register(DailyTimeLog,DailyTimeLogAdmin)
admin.site.register(Reimbursement, ReimbursementAdmin)
admin.site.register(LeaveManagement, LeaveManagementAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Employee,EmployeeAdmin)


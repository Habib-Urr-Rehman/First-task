"""
URL configuration for finalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login),
    path('company_detail/', views.company_detail),
    path('add_company/',views.company_add),
    path('delete_company/<int:id>',views.company_delete),
    path('edit_company/<int:id>/', views.company_edit, name='company_edit'),
    path('departments_detail/', views.department_detail),
    path('add_department/',views.department_add),
    path('delete_department/<int:id>',views.department_delete),
    path('edit_department/<int:id>/', views.department_edit, name='department_edit'),
    path('company_detail/<int:pk>/departments/', views.company_departments),
    path('company_detail/<int:pk>/projects/', views.company_projects),
    path('company_detail/<int:pk>/employees/', views.company_employeess),
    path('projects_detail/',views.project_detail),
    path('add_project/',views.project_add),
    path('delete_project/<int:id>',views.project_delete),
    path('edit_project/<int:id>/', views.project_edit, name='project_edit'),
    path('employees_detail/', views.employee_detail, name='employee_detail'),
    path('delete_employee/<int:id>/', views.employee_delete, name='employee_delete'),
    path('get_departments/<int:company_id>/', views.get_departments, name='get_departments'),
    path('get_projects/<int:company_id>/', views.get_projects, name='get_projects'),
    path('leave_detail/', views.leave_details),
    path('add_leave/', views.leave_add),
    path('delete_leaves/<int:id>/', views.leave_delete),
    path('edit_leaves/<int:id>/', views.leave_edit, name='leave_edit'),
    path('reimbursement_detail/', views.reimbursement_details),
    path('add_reimbursement/', views.reimbursement_add, name='reimbursement_add'),
    path('edit_reimbursements/<int:id>/', views.reimbursement_edit, name='reimbursement_edit'),
    path('delete_reimbursements/<int:id>/', views.reimbursement_delete, name='reimbursement_delete'),
    path('approved_reimbursements/', views.approved_reimbursements, name='approved_reimbursements'),
    path('approved_leaves/', views.approved_leaves, name='approved_leaves'),
    path('time_tracking_detail/', views.time_tracking_detail, name='time_tracking_detail'),
    path('add_time_tracking/', views.time_tracking_add),
    path('delete_time_tracking/<int:id>/', views.time_tracking_delete, name='delete_time_tracking'),
    path('edit_time_tracking/<int:id>/', views.time_tracking_edit, name='edit_time_tracking'),
    path('time_tracking/<int:time_tracking_id>/', views.daily_time_log_detail, name='daily_time_log_detail'),
    path('signup/',views.user_signup),
    path('login/',views.user_login),
    path('performance_review/', views.performance_review_detail, name='performance_review_detail'),
    path('edit_performance_review/<int:review_id>/', views.edit_performance_review, name='edit_performance_review'),
    path('delete_performance_review/<int:review_id>/', views.delete_performance_review, name='delete_performance_review'),
    path('training/', views.training_detail, name='training_detail'),
    path('edit_training/<int:training_id>/', views.edit_training, name='edit_training'),
    path('delete_training/<int:training_id>/', views.delete_training, name='delete_training'),
    path('employee_add_first/', views.employee_add_first),
]


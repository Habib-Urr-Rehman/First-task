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
    path('', views.company_deatil),
    path('company_detail/', views.company_deatil),
    path('add_company/',views.company_add),
    path('delete_company/<int:ij>',views.company_delete),
    path('edit_company/<int:id>/', views.company_edit, name='company_edit'),
    path('departments_detail/', views.department_detail),
    path('add_department/',views.department_add),
    path('delete_department/<int:id>',views.department_delete),
    path('edit_department/<int:id>/', views.department_edit, name='department_edit'),
    path('company_detail/<int:pk>/departments/', views.company_departments),
    path('projects_detail/',views.project_detail),
    path('add_project/',views.project_add),
    path('delete_project/<int:id>',views.project_delete),
    path('edit_project/<int:id>/', views.project_edit, name='project_edit'),
    path('navbar/', views.index),
    path('employees_detail/', views.employee_detail),
    path('add_employee/', views.employee_add),
    path('delete_employee/<int:id>',views.employee_delete),
    path('edit_employee/<int:id>/', views.employee_edit, name='employee_edit'),
    path('get_departments/<int:company_id>/', views.get_departments, name='get_departments'),
    path('get_projects/<int:company_id>/', views.get_projects, name='get_projects'),
]


from django.contrib import admin
from django.urls import path
from apiviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', views.company_api),
    path('companies/<int:pk>/', views.company_api),
    path('employees/', views.employee_api),
    path('employees/<int:pk>/', views.employee_api),
    path('projects/', views.project_api),
    path('projects/<int:pk>/', views.project_api),
    path('departments/', views.department_api),
    path('departments/<int:pk>/', views.department_api),
    path('hrdepartments/', views.hr_department_api),
    path('hrdepartments/<int:pk>/', views.hr_department_api),
    path('companies/<int:pk>/employees/', views.company_employees),
    path('companies/<int:pk>/projects/', views.company_projects),
    path('companies/<int:pk>/departments/', views.company_departments),
    path('projects/<int:pk>/employees/', views.project_employees),
]


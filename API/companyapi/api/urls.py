from django.contrib import admin
from django.urls import path,include
from api.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)
router.register(r'projects', ProjectViewSet)  
router.register(r'departments', DepartmentViewSet)
router.register(r'hrdepartments', HrDepartmentViewSet)
urlpatterns = [
    path('',include(router.urls)),
]


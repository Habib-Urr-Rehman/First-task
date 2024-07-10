from apiviews.models import *
from rest_framework import serializers
       
class CompanySerializer(serializers.ModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model= Company
        fields="__all__"
        
class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= Employee
        fields="__all__"

class ProjectsSerializer(serializers.ModelSerializer):
    project_id=serializers.ReadOnlyField()
    class Meta:
        model= Project
        fields="__all__"

class DepartmentSerilizer(serializers.ModelSerializer):
    department_id=serializers.ReadOnlyField()
    class Meta:
        model= Department
        fields="__all__"

class HrDepartmentSerilizer(serializers.ModelSerializer):
    department_id=serializers.ReadOnlyField()
    class Meta:
        model= HrDepartment
        fields="__all__"


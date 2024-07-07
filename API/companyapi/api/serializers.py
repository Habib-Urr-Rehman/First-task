from api.models import *
from rest_framework import serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model= Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= Employee
        fields="__all__"

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    project_id=serializers.ReadOnlyField()
    class Meta:
        model= Project
        fields="__all__"

class DepartmentSerilizer(serializers.HyperlinkedModelSerializer):
    department_id=serializers.ReadOnlyField()
    class Meta:
        model= Department
        fields="__all__"

class HrDepartmentSerilizer(serializers.HyperlinkedModelSerializer):
    department_id=serializers.ReadOnlyField()
    class Meta:
        model= HrDepartment
        fields="__all__"

from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    # URL companies/{companyID}/employees
    @action (detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            companies = get_object_or_404(Company, pk=pk)
            emps=Employee.objects.filter(company=companies)
            emps_serializers=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(  emps_serializers.data)
        except Exception as e:
            return Response({
            'message':e
        })

    # URL compies/{companyID}/projects
    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        try:
            company = get_object_or_404(Company, pk=pk)
            projects = Project.objects.filter(company=company)
            serializer = ProjectsSerializer(projects, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': str(e)})
        
    # URL compies/{companyID}/departments
    @action(detail=True, methods=['get'])
    def departments(self, request, pk=None):
        try:
            company = get_object_or_404(Company, pk=pk)
            departments = Department.objects.filter(company=company)
            serializer = DepartmentSerilizer(departments, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': str(e)})

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

      # URL projects/{projectID}/employees
    @action (detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            project = get_object_or_404(Project, pk=pk)
            emps=project.employees.all()
            emps_serializers=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(  emps_serializers.data)
        except Exception as e:
            return Response({
            'message':e
        })

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerilizer

class HrDepartmentViewSet(viewsets.ModelViewSet):
    queryset = HrDepartment.objects.all()
    serializer_class = HrDepartmentSerilizer
    
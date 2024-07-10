from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apiviews.models import *
from apiviews.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def company_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            company = get_object_or_404(Company, pk=pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PUT':
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PATCH':
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        company = get_object_or_404(Company, pk=pk)
        company.delete()
        return Response({'msg':'Company Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def employee_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            employee = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PUT':
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PATCH':
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response({'msg':'Employee Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def project_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            project = get_object_or_404(Project, pk=pk)
            serializer = ProjectsSerializer(project)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            projects = Project.objects.all()
            serializer = ProjectsSerializer(projects, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializer=ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PUT':
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectsSerializer(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PATCH':
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectsSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return Response({'msg':'Project Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def department_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            department = get_object_or_404(Department, pk=pk)
            serializer = DepartmentSerilizer(department)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            departments = Department.objects.all()
            serializer = DepartmentSerilizer(departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = DepartmentSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Department Created Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerilizer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Department Updated Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        department = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerilizer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Department Updated Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        department = get_object_or_404(Department, pk=pk)
        department.delete()
        return Response({'msg': 'Department Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def hr_department_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            hr_department = get_object_or_404(HrDepartment, pk=pk)
            serializer = HrDepartmentSerilizer(hr_department)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            hr_departments = HrDepartment.objects.all()
            serializer = HrDepartmentSerilizer(hr_departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = HrDepartmentSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'HR Department Created Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        hr_department = get_object_or_404(HrDepartment, pk=pk)
        serializer = HrDepartmentSerilizer(hr_department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'HR Department Updated Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        hr_department = get_object_or_404(HrDepartment, pk=pk)
        serializer = HrDepartmentSerilizer(hr_department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'HR Department Updated Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        hr_department = get_object_or_404(HrDepartment, pk=pk)
        hr_department.delete()
        return Response({'msg': 'HR Department Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# URL compies/{companyID}/employees
@api_view(['GET'])
def company_employees(request, pk):
    company = get_object_or_404(Company, pk=pk)
    employees = Employee.objects.filter(company=company)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

# URL compies/{companyID}/projects
@api_view(['GET'])
def company_projects(request, pk):
    company = get_object_or_404(Company, pk=pk)
    projects = Project.objects.filter(company=company)
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data)

# URL compies/{companyID}/departments
@api_view(['GET'])
def company_departments(request, pk):
    company = get_object_or_404(Company, pk=pk)
    departments = Department.objects.filter(company=company)
    serializer = DepartmentSerilizer(departments, many=True)
    return Response(serializer.data)

# URL projects/{projectID}/employees
@api_view(['GET'])
def project_employees(request,pk):
    project = get_object_or_404(Project, pk=pk)
    employee_data=project.employees.all()
    employees_serializers=EmployeeSerializer(employee_data,many=True)
    return Response(employees_serializers.data)
           
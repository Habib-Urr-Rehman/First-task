from django.shortcuts import render
from django.shortcuts import redirect
from employee_management.models import * 
from django.shortcuts import get_object_or_404,HttpResponse
from django.http import JsonResponse

def company_deatil(request):
    Companies=Company.objects.all()
    context = {
        'companies': Companies,
        'type_choices': TYPE_CHOICES
    }
    return render (request,'company.html',context)

def company_add(request):
    if request.method == 'POST':
        Company.objects.create(
            name=request.POST.get("name"),
            location=request.POST.get("location"),
            about=request.POST.get("about"),
            type=request.POST.get("type"),
            active=request.POST.get("active") == 'True'  
        )
        return redirect('/company_detail')
    return render(request, 'company.html',{})

def company_delete(request,ij):
    company=get_object_or_404(Company,pk=ij)
    company.delete()
    return redirect('/company_detail')
    
def company_edit(request, id):
    company = get_object_or_404(Company, pk=id)
    if request.method == 'POST':
        company.name = request.POST.get("name")
        company.location = request.POST.get("location")
        company.about = request.POST.get("about")
        company.type = request.POST.get("type")
        company.active = request.POST.get("active") == 'True'
        company.save()
        return redirect('/company_detail')
    else:
        context = {
            'company': company,
            'type_choices': TYPE_CHOICES,
        }
        return render(request, 'edit_company.html', context)
    
def department_detail(request):
    departments = Department.objects.all()
    companies = Company.objects.all() 
    return render(request, 'department_detail.html', {'departments': departments, 'companies': companies})

def department_add(request):
    if request.method == 'POST':
        company_idd = request.POST.get("comp")
        company=get_object_or_404(Company,pk=company_idd)

        Department.objects.create(
            name=request.POST.get("name"),
            company=company,  
        )
        return redirect('/departments_detail')
    companies = Company.objects.all()
    return render(request, 'department_detail.html', {'companies': companies})

def department_delete(request,id):
    department=get_object_or_404(Department,pk=id)
    department.delete()
    return redirect('/departments_detail')

def department_edit(request, id):
    companies = Company.objects.all()
    department = get_object_or_404(Department, pk=id)
    if request.method == 'POST':
        department.name = request.POST.get("name")
        company_id = request.POST.get("comp")
        company = get_object_or_404(Company, pk=company_id)
        department.company = company
        department.save()
        return redirect('/departments_detail')
    
    return render(request, 'edit_department.html', {'departments': department, 'companies': companies})

def company_departments(request, pk):
    company = get_object_or_404(Company, pk=pk)
    departments = Department.objects.filter(company=company)
    return render(request, 'company_departments.html', {'company': company, 'departments': departments})

def project_detail(request):
    projects= Project.objects.all()
    companies = Company.objects.all() 
    return render(request, 'project_detail.html', {'projects': projects, 'companies': companies})

def project_add(request):
    if request.method == 'POST':
        company_id = request.POST.get("comp")
        company=get_object_or_404(Company,pk=company_id)

        Project.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            start_date=request.POST.get("start_date"),
            end_date=request.POST.get("end_date"),
            company=company,  
        )
        return redirect('/projects_detail')
    companies = Company.objects.all()
    return render(request, 'project_detail.html', {'companies': companies})

def project_delete(request,id):
    project=get_object_or_404(Project,pk=id)
    project.delete()
    return redirect('/projects_detail')

def project_edit(request, id):
    companies = Company.objects.all()
    project = get_object_or_404(Project, pk=id)  
    if request.method == 'POST':
        project.name = request.POST.get("name")
        company_id = request.POST.get("comp")
        company = get_object_or_404(Company, pk=company_id)
        project.company = company
        project.description = request.POST.get("description")
        project.start_date = request.POST.get("start_date")
        project.end_date = request.POST.get("end_date")
        project.save()
        return redirect('/projects_detail')
    return render(request, 'edit_project.html', {'projects': project, 'companies': companies})

def index(request):
    return render(request,'base.html',{})

def employee_detail(request):
    Employees=Employee.objects.all()
    Companies=Company.objects.all()
    Departments=Department.objects.all()
    Projects=Project.objects.all()
    context={
        'employees':Employees,
        'position_choices':POSITION_CHOICES,
        'companies':Companies,
        'departments':Departments,
        'projects':Projects
    }
    return render(request,'employee_detail.html',context)


def employee_add(request):
    if request.method == 'POST':
        company_id = request.POST.get("company")
        company = get_object_or_404(Company, pk=company_id)
        department_id = request.POST.get("department")
        department = get_object_or_404(Department, pk=department_id)
        project_id = request.POST.get("project")
        project = get_object_or_404(Project, pk=project_id)

        Employee.objects.create(
            name = request.POST.get("name"),
            email = request.POST.get("email"),
            address = request.POST.get("address"),
            phone = request.POST.get("phone"),
            about = request.POST.get("about"),
            position = request.POST.get("position"),
            company = company, 
            department = department,
            project = project
        )
        return redirect('/employees_detail')
    else:
        Employees = Employee.objects.all()
        Companies = Company.objects.all()
        Departments = Department.objects.all()
        Projects = Project.objects.all()
    
    context = {
        'employees': Employees,
        'position_choices': POSITION_CHOICES,
        'companies': Companies,
        'departments': Departments,
        'projects': Projects
    }
  
    return render(request, 'employee_detail.html', context)

def employee_delete(request,id):
    employee=get_object_or_404(Employee,pk=id)
    employee.delete()
    return redirect('/employees_detail')


def employee_edit(request, id):
    employee = get_object_or_404(Employee, pk=id)
    companies = Company.objects.all()
    departments = Department.objects.all()
    projects = Project.objects.all()

    if request.method == 'POST':
        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.address = request.POST.get("address")
        employee.phone = request.POST.get("phone")
        employee.about = request.POST.get("about")
        employee.position = request.POST.get("position")
        
        company_id = request.POST.get("company")
        company = get_object_or_404(Company, pk=company_id)
        employee.company = company
        
        department_id = request.POST.get("department")
        department = get_object_or_404(Department, pk=department_id)
        employee.department = department
        
        project_id = request.POST.get("project")
        project = get_object_or_404(Project, pk=project_id)
        employee.project = project
        
        employee.save()
        return redirect('/employees_detail')

    context = {
        'employee': employee,
        'companies': companies,
        'departments': departments,
        'projects': projects,
        'position_choices': POSITION_CHOICES,
    }

    return render(request, 'edit_employee.html', context)

def get_departments(request, company_id):
    departments = Department.objects.filter(company_id=company_id)
    department_list = list(departments.values('department_id', 'name'))
    return JsonResponse(department_list, safe=False)

def get_projects(request, company_id):
    projects = Project.objects.filter(company_id=company_id)
    project_list = list(projects.values('project_id', 'name'))
    return JsonResponse(project_list, safe=False)


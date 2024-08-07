from django.shortcuts import render
from django.shortcuts import redirect
from employee_management.models import * 
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.http import HttpResponseBadRequest

def company_detail(request):
    Companies = Company.objects.all()
    context = {
        'companies': Companies,
        'type_choices': TYPE_CHOICES,
        'user_role': request.user.role
        
    }
    return render (request,'company.html',context)

@login_required
def company_add(request):
    if request.user.role != 'admin':
        return redirect('/company_detail')
    
    if request.method == 'POST':
        Company.objects.create(
            name = request.POST.get("name"),
            location = request.POST.get("location"),
            about = request.POST.get("about"),
            type = request.POST.get("type"),
            active = request.POST.get("active") == 'True'  
        )
        return redirect('/company_detail')
    
    return render(request, 'company.html', {'user_role': request.user.role})

@login_required
def company_delete(request, id):
    if request.user.role != 'admin':
        return redirect('/company_detail')

    company = get_object_or_404(Company, pk=id)
    company.delete()
    return redirect('/company_detail')
    
@login_required
def company_edit(request, id):
    if request.user.role != 'admin':
        return redirect('/company_detail')

    company = get_object_or_404(Company, pk=id)

    if request.method == 'POST':
        company.name = request.POST.get("name")
        company.location = request.POST.get("location")
        company.about = request.POST.get("about")
        company.type = request.POST.get("type")
        company.active = request.POST.get("active") == 'True'
        company.save()
        return redirect('/company_detail')

    context = {
        'company': company,
        'type_choices': TYPE_CHOICES,
        'user_role': request.user.role
    }
    return render(request, 'edit_company.html', context)

@login_required
def department_detail(request):
    departments = Department.objects.all()
    companies = Company.objects.all()
    context = {
        'departments': departments,
        'companies': companies,
        'user_role': request.user.role
    }
    return render(request, 'department_detail.html', context)

@login_required
def department_add(request):
    if request.user.role != 'admin':
        return redirect('/departments_detail')

    if request.method == 'POST':
        company_id = request.POST.get("company")
        company = get_object_or_404(Company, pk=company_id)

        Department.objects.create(
            name = request.POST.get("name"),
            company = company
        )
        return redirect('/departments_detail')

    companies = Company.objects.all()
    return render(request, 'department_detail.html', {'companies': companies, 'user_role': request.user.role})

@login_required
def department_delete(request, id):
    if request.user.role != 'admin':
        return redirect('/departments_detail')

    department = get_object_or_404(Department, pk=id)
    department.delete()
    return redirect('/departments_detail')

@login_required
def department_edit(request, id):
    if request.user.role != 'admin':
        return redirect('/departments_detail')

    department = get_object_or_404(Department, pk=id)
    companies = Company.objects.all()

    if request.method == 'POST':
        department.name = request.POST.get("name")
        company_id = request.POST.get("company")
        company = get_object_or_404(Company, pk=company_id)
        department.company = company
        department.save()
        return redirect('/departments_detail')

    context = {
        'departments': department,
        'companies': companies,
        'user_role': request.user.role
    }
    return render(request, 'edit_department.html', context)

def company_departments(request, pk):
    company = get_object_or_404(Company, pk=pk)
    departments = Department.objects.filter(company=company)
    return render(request, 'company_departments.html', {'company': company, 'departments': departments})

def company_projects(request, pk):
    company = get_object_or_404(Company, pk=pk)
    projects = Project.objects.filter(company=company)
    return render(request, 'company_projects.html', {'company': company, 'projects': projects})

def company_employeess(request, pk):
    company = get_object_or_404(Company, pk=pk)
    employees = Employee.objects.filter(company=company)
    return render(request, 'company_employees.html', {'company': company, 'employees': employees})

@login_required
def project_detail(request):
    projects = Project.objects.all()
    companies = Company.objects.all()
    return render(request, 'project_detail.html', {'projects': projects, 'companies': companies, 'user_role': request.user.role})

@login_required
def project_add(request):
    if request.user.role != 'admin':
        return redirect('/projects_detail')
    
    if request.method == 'POST':
        company_id = request.POST.get("company")
        company = get_object_or_404(Company, pk=company_id)
        
        Project.objects.create(
            name = request.POST.get("name"),
            description = request.POST.get("description"),
            start_date = request.POST.get("start_date"),
            end_date = request.POST.get("end_date"),
            company = company
        )
        return redirect('/projects_detail')

    companies = Company.objects.all()
    return render(request, 'project_detail.html', {'companies': companies, 'user_role': request.user.role})

@login_required
def project_delete(request, id):
    if request.user.role != 'admin':
        return redirect('/projects_detail')
    
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('/projects_detail')

@login_required
def project_edit(request, id):
    if request.user.role != 'admin':
        return redirect('/projects_detail')

    companies = Company.objects.all()
    project = get_object_or_404(Project, pk=id)

    if request.method == 'POST':
        project.name = request.POST.get("name")
        company_id = request.POST.get("company")
        company = get_object_or_404(Company, pk=company_id)
        project.company = company
        project.description = request.POST.get("description")
        project.start_date = request.POST.get("start_date")
        project.end_date = request.POST.get("end_date")
        project.save()
        return redirect('/projects_detail')

    return render(request, 'edit_project.html', {'projects': project, 'companies': companies,'user_role': request.user.role})

@login_required
def employee_detail(request):
    employees = Employee.objects.all()
    companies = Company.objects.all()
    departments = Department.objects.all()
    projects = Project.objects.all()
    context = {
        'employees': employees,
        'position_choices': POSITION_CHOICES,
        'companies': companies,
        'departments': departments,
        'projects': projects,
        'user_role': request.user.role
    }
    return render(request, 'employee_detail.html', context)

@login_required
def employee_delete(request, id):
    if request.user.role != 'admin':
        return redirect('/employees_detail')

    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('/employees_detail')

def get_departments(request, company_id):
    departments = Department.objects.filter(company_id = company_id)
    department_list = list(departments.values('department_id', 'name'))
    return JsonResponse(department_list, safe = False)

def get_projects(request, company_id):
    projects = Project.objects.filter(company_id = company_id)
    project_list = list(projects.values('project_id', 'name'))
    return JsonResponse(project_list, safe = False)

@login_required
def approved_leaves(request):
    user = request.user

    if user.role == 'admin':
        approved_leaves = LeaveManagement.objects.filter(is_approved=True)
    else:
        approved_leaves = LeaveManagement.objects.filter(employee=user.employee, is_approved=True)
    
    context = {
        'approved_leaves': approved_leaves,
    }
    return render(request, 'approved_leaves.html', context)

@login_required
def leave_edit(request, id):
    leave = get_object_or_404(LeaveManagement, pk=id)
    user = request.user

    if request.method == 'POST':
        employee_id = request.POST.get("employee")

        if user.role == 'admin':
            employee = get_object_or_404(Employee, pk=employee_id)
        else:
            employee = user.employee
        
        leave.employee = employee
        leave.leave_type = request.POST.get('type')
        leave.start_date = request.POST.get("start_date")
        leave.end_date = request.POST.get("end_date")
        leave.save()
        return redirect('/leave_detail')  
    
    if user.role == 'admin':
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.filter(id=user.employee.id)
    
    context = {
        'leave': leave,  
        'employees': employees,
        'type_choices': LEAVE_TYPE_CHOICES,
    }
    return render(request, 'edit_leaves.html', context)

@login_required
def leave_delete(request, id):
    leave = get_object_or_404(LeaveManagement, pk=id)
    leave.delete()
    return redirect('/leave_detail')  

@login_required
def leave_details(request):
    if request.user.role == 'admin':
        leaves = LeaveManagement.objects.all()
    else:
        leaves = LeaveManagement.objects.filter(employee__user=request.user)

    context = {
        'leaves': leaves,
        'type_choices': LEAVE_TYPE_CHOICES,
        'employees': Employee.objects.all()  
    }
    return render(request, 'leave_detail.html', context)

@login_required
def leave_add(request):
    user = request.user
    if request.method == 'POST':
        employee_id = request.POST.get("employee")
        employee = get_object_or_404(Employee, pk=employee_id)
        LeaveManagement.objects.create(
            employee = employee,
            leave_type = request.POST.get("type"),
            start_date = request.POST.get("start_date"),
            end_date = request.POST.get("end_date"),
        )
        return redirect('/leave_detail/')
    
    leaves = LeaveManagement.objects.all()
    employees = Employee.objects.all()
    if user.role == 'employee':
        employees = employees.filter(id=user.employee.id)
    context = {
        'leaves': leaves,
        'employees': employees,
        'type_choices': LEAVE_TYPE_CHOICES
    }
    return render(request, 'leave_detail.html', context)

@login_required
def reimbursement_details(request):
    if request.user.role == 'admin':
        reimbursements = Reimbursement.objects.all()
    else:
        reimbursements = Reimbursement.objects.filter(employee__user = request.user)

    context = {
        'reimbursements': reimbursements,
        'type_choices': REIMBURSEMENT_TYPE_CHOICES,
        'employees': Employee.objects.all() 
    }
    return render(request, 'reimbursement_detail.html', context)

@login_required
def reimbursement_add(request):
    user = request.user
    if request.method == 'POST':
        employee_id = request.POST.get("employee")
        employee = get_object_or_404(Employee, pk=employee_id)
        Reimbursement.objects.create(
            employee = employee,
            type = request.POST.get("type"),
            amount = request.POST.get("amount"),
            date = request.POST.get("date"),
        )
        return redirect('reimbursement_detail')
    
    employees = Employee.objects.all()
    if user.role == 'employee':
        employees = employees.filter(id=user.employee.id)
    context = {
        'employees': employees,
        'type_choices': REIMBURSEMENT_TYPE_CHOICES
    }
    return render(request, 'reimbursement_detail.html', context)

@login_required
def reimbursement_edit(request, id):
    reimbursement = get_object_or_404(Reimbursement, pk=id)
    user = request.user

    if request.method == 'POST':
        employee_id = request.POST.get("employee")
        if user.role == 'admin':
            employee = get_object_or_404(Employee, pk=employee_id)
        else:
            employee = user.employee
        
        reimbursement.employee = employee
        reimbursement.type = request.POST.get('type')
        reimbursement.amount = request.POST.get('amount')
        reimbursement.date = request.POST.get('date')
        reimbursement.save()
        return redirect('/reimbursement_detail/')
    
    if user.role == 'admin':
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.filter(id=user.employee.id)
    
    context = {
        'reimbursement': reimbursement,
        'employees': employees,
        'type_choices': REIMBURSEMENT_TYPE_CHOICES,
    }
    return render(request, 'edit_reimbursements.html', context)

@login_required
def reimbursement_delete(request, id):
    reimbursement = get_object_or_404(Reimbursement, pk=id)
    reimbursement.delete()
    return redirect('/reimbursement_detail/')

@login_required
def approved_reimbursements(request):
    user = request.user
    if user.role == 'admin':
        approved_reimbursements = Reimbursement.objects.filter(status=True)
    else:
        approved_reimbursements = Reimbursement.objects.filter(employee=user.employee, status=True)
    
    context = {
        'approved_reimbursements':approved_reimbursements,
    }
    return render(request, 'approved_reimbursements.html', context)

def user_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect("/signup/")

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect("/signup/")

        user = CustomUser(username=username, email=email)
        user.set_password(password1)  # Hash the password
        user.save()

        messages.success(request, 'Account successfully created')
        return redirect("/login/")
    
    return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if the user is an admin
            if user.is_superuser or user.role == 'admin':
                return redirect('/company_detail/')
            # Check if the user is already an employee
            elif hasattr(user, 'employee'):
                return redirect('/company_detail/')
            else:
                return redirect('/employee_add_first/')
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect('/login/')
    
    return render(request, 'login.html')

@login_required
def time_tracking_detail(request):
    user = request.user

    if user.role == 'admin':
        time_trackings = TimeTracking.objects.all()
    else:
        if hasattr(user, 'employee'):
            time_trackings = TimeTracking.objects.filter(employee=user.employee)
        else:
            time_trackings = TimeTracking.objects.none()  

    context = {
        'time_trackings': time_trackings,
        'employees': Employee.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'time_tracking_detail.html', context)


@login_required
def time_tracking_add(request):
    user = request.user
    if request.method == 'POST':
        employee_id = request.POST.get("employee")
        project_id = request.POST.get("project")
        employee = get_object_or_404(Employee, pk=employee_id)
        project = get_object_or_404(Project, pk=project_id)

        TimeTracking.objects.create(
            employee = employee,
            project = project,
            date = request.POST.get("date"),
        )
        return redirect('/time_tracking_detail/')

    if user.role == 'employee':
        employees = Employee.objects.filter(id=user.employee.id)
    else:
        employees = Employee.objects.all()

    projects = Project.objects.all()
    context = {
        'employees': employees,
        'projects': projects,
    }
    return render(request, 'add_time_tracking.html', context)

@login_required
def time_tracking_delete(request, id):
    user = request.user
    time_tracking = get_object_or_404(TimeTracking, pk=id)
    if user.role == 'admin' or time_tracking.employee == user.employee:
        time_tracking.delete()
    return redirect('/time_tracking_detail/')

@login_required
def time_tracking_edit(request, id):
    time_tracking = get_object_or_404(TimeTracking, pk=id)
    user = request.user

    if request.method == 'POST':
        employee_id = request.POST.get("employee")
        project_id = request.POST.get("project")

        if user.role == 'admin':
            employee = get_object_or_404(Employee, pk=employee_id)
        else:
            employee = user.employee

        project = get_object_or_404(Project, pk=project_id)
        time_tracking.employee = employee
        time_tracking.project = project
        time_tracking.date = request.POST.get("date")
        time_tracking.save()
        return redirect('/time_tracking_detail/')

    if user.role == 'admin':
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.filter(id=user.employee.id)

    projects = Project.objects.all()
    context = {
        'time_tracking': time_tracking,
        'employees': employees,
        'projects': projects,
    }
    return render(request, 'edit_time_tracking.html', context)

@login_required
def daily_time_log_detail(request, time_tracking_id):
    time_tracking = get_object_or_404(TimeTracking, id=time_tracking_id)
    daily_logs = DailyTimeLog.objects.filter(time_tracking=time_tracking)

    if request.method == 'POST':
        hours = request.POST.get("hours")
        task_type = request.POST.get("task_type")
        description = request.POST.get("description")
        
        if hours and task_type and description:
            DailyTimeLog.objects.create(
                time_tracking=time_tracking,
                hours=hours,
                task_type=task_type,
                description=description
            )
            return redirect('daily_time_log_detail', time_tracking_id=time_tracking.id)

    context = {
        'daily_logs': daily_logs,
        'task_choices': TASK_CHOICES,
        'time_tracking': time_tracking
    }
    return render(request, 'daily_time_log_detail.html', context)

@login_required
def performance_review_detail(request):
    performance_reviews = PerformanceReview.objects.all()
    employees = Employee.objects.all()

    if request.method == 'POST':
        employee_id = request.POST.get("employee")
        review_date = request.POST.get("review_date")
        performance_score = request.POST.get("performance_score")
        comments = request.POST.get("comments")
        
        if employee_id and review_date and performance_score and comments:
            PerformanceReview.objects.create(
                employee_id=employee_id,
                review_date=review_date,
                performance_score=performance_score,
                comments=comments
            )
            return redirect('performance_review_detail')

    context = {
        'performance_reviews': performance_reviews,
        'employees': employees,
    }
    return render(request, 'performance_review_detail.html', context)

@login_required
def training_detail(request):
    trainings = Training.objects.prefetch_related('participants').all()
    employees = Employee.objects.all()

    if request.method == 'POST':
        name = request.POST.get("name")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        participant_ids = request.POST.getlist("participants")

        if name and start_date and end_date and participant_ids:
            training = Training.objects.create(
                name=name,
                start_date=start_date,
                end_date=end_date
            )
            training.participants.set(participant_ids)
            return redirect('training_detail')

    context = {
        'trainings': trainings,
        'employees': employees,
    }
    return render(request, 'training_detail.html', context)

login_required
def edit_performance_review(request, review_id):
    review = get_object_or_404(PerformanceReview, id=review_id)
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        review_date = request.POST.get('review_date')
        performance_score = request.POST.get('performance_score')
        comments = request.POST.get('comments')
        
        review.employee_id = employee_id
        review.review_date = review_date
        review.performance_score = performance_score
        review.comments = comments
        review.save()
        return redirect('performance_review_detail')
    else:
        employees = Employee.objects.all()
        context = {
            'review': review,
            'employees': employees
        }
        return render(request, 'edit_performance_review.html', context)
    
@login_required
def delete_performance_review(request, review_id):
    review = get_object_or_404(PerformanceReview, id=review_id)
    review.delete()
    return redirect('performance_review_detail')

@login_required
def edit_training(request, training_id):
    training = get_object_or_404(Training, id=training_id)
    employees = Employee.objects.all()

    if request.method == 'POST':
        training.name = request.POST.get("name")
        training.start_date = request.POST.get("start_date")
        training.end_date = request.POST.get("end_date")
        participant_ids = request.POST.getlist("participants")
        training.participants.set(participant_ids)
        training.save()
        return redirect('training_detail')

    context = {
        'training': training,
        'employees': employees,
    }
    return render(request, 'edit_training.html', context)

@login_required
def delete_training(request, training_id):
    training = get_object_or_404(Training, id=training_id)
    training.delete()
    return redirect('training_detail')

@login_required
def employee_add_first(request):
    if request.method == 'POST':
        company_id = request.POST.get("company")
        department_id = request.POST.get("department")
        project_id = request.POST.get("project")
        user_id = request.POST.get("user")

        # Verify and convert IDs
        try:
            department_id = int(department_id) if department_id else None
            project_id = int(project_id) if project_id else None
        except ValueError:
            # Handle the case where conversion fails
            return HttpResponseBadRequest("Invalid department or project ID")

        company = get_object_or_404(Company, pk=company_id)
        department = get_object_or_404(Department, pk=department_id) if department_id else None
        project = get_object_or_404(Project, pk=project_id) if project_id else None
        user = get_object_or_404(CustomUser, pk=user_id)

        Employee.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            address=request.POST.get("address"),
            phone=request.POST.get("phone"),
            about=request.POST.get("about"),
            position=request.POST.get("position"),
            company=company,
            department=department,
            project=project,
            user=user
        )
        return redirect('/employees_detail')
    
    else:
        Employees = Employee.objects.all()
        Companies = Company.objects.all()
        Departments = Department.objects.all()
        Projects = Project.objects.all()
        Users = CustomUser.objects.filter(employee__isnull=True).exclude(is_superuser=True)
        context = {
            'employees': Employees,
            'position_choices': POSITION_CHOICES,
            'companies': Companies,
            'departments': Departments,
            'projects': Projects,
            'users': Users,
            'user_role': request.user.role
        }
    
        return render(request, 'employee_add_first.html', context)


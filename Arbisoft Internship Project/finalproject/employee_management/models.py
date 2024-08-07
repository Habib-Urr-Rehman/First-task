from django.db import models
from django.contrib.auth.models import AbstractUser
from employee_management.constants import *

class CustomUser(AbstractUser):
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='employee')
    
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DepartmentRolesAccess(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    leave_approval = models.BooleanField(default=False)
    reimbursement_approval = models.BooleanField(default=False)

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
   
class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee',null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, unique=True)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    performance_score = models.PositiveIntegerField()
    comments = models.TextField()

class Training(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(Employee)

class TimeTracking(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()

class DailyTimeLog(models.Model):    
    time_tracking = models.ForeignKey(TimeTracking, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=4, decimal_places=2)
    task_type = models.CharField(max_length=20, choices=TASK_CHOICES)
    description = models.TextField()

class Reimbursement(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=REIMBURSEMENT_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.BooleanField(default=False) 

class LeaveManagement(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)  


from django.db import models

# Choices constants
POSITION_CHOICES = (
    ('Manager', 'Manager'),
    ('Software Developer', 'Software Developer'),
    ('Project Leader', 'Project Leader'),
)

TYPE_CHOICES = (
    ('IT', 'IT'),
    ('Non IT', 'Non IT'),
    ('Mobile Phones', 'Mobile Phones'),
)

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=TYPE_CHOICES)
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    department_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
   #inheritance 
class HrDepartment(Department):
    hr_name = models.CharField(max_length=100)

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=15,unique=True)
    about=models.TextField()
    postion=models.CharField(max_length=20,choices=POSITION_CHOICES)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee)
    
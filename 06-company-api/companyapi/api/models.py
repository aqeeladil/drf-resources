from django.db import models

# Create your models here.


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), 
                                                     ('Finance', 'Finance'), 
                                                     ('Health', 'Health'), 
                                                     ('Mobiles', 'Mobiles')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    position = models.CharField(max_length=50, choices=(('Manager', 'Manager'),
                                                         ('Developer', 'Developer'),
                                                         ('Designer', 'Designer'),
                                                         ('Tester', 'Tester')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
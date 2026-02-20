from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.location}"  

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField(default='2024-01-01')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    department= models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
    report_to = models.ForeignKey('self',on_delete=models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
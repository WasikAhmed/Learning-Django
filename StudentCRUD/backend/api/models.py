from django.db import models

class Department(models.Model):
    department_name = models.CharField("Department Name", max_length=100)

    def __str__(self):
        return self.department_name
    
class Student(models.Model):
    student_id = models.CharField("Student Id", max_length=20, unique=True)
    student_name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    date_of_birth = models.DateField("Date of Birth")
    address = models.TextField("Address")
    phone = models.CharField("Phone", max_length=20)

    def __str__(self):
        return self.student_id


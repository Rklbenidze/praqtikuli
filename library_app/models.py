from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="departments", null=True
    )

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class JobPosition(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="positions"
    )

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=128)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
    )
    position = models.ForeignKey(
        JobPosition,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeProfile(models.Model):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="profile")
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    skills = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f"{self.employee}'s profile"


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    employees = models.ManyToManyField(
        Employee, related_name="projects", blank=True
    )

    def __str__(self):
        return self.name

    


    




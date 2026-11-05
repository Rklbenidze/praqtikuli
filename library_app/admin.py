from django.contrib import admin
from .models import Company, Department, JobPosition, Employee, EmployeeProfile, Project

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(JobPosition)
admin.site.register(Employee)
admin.site.register(EmployeeProfile)
admin.site.register(Project)


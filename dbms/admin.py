from django.contrib import admin

# Register your models here.

from .models import Student,Teachers, Admin
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Teachers)
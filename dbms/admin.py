from django.contrib import admin

# Register your models here.

from .models import Student,Teachers, Admin,Img
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Teachers)
admin.site.register(Img)
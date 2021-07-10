from django.contrib import admin

# Register your models here.

from .models import Student,Teachers, Admin,Img,Videos,Enroll,Exam,Quiz
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Teachers)
admin.site.register(Img)
admin.site.register(Videos)
admin.site.register(Enroll)
admin.site.register(Exam)
admin.site.register(Quiz)
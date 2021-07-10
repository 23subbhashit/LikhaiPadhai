from django.db import models
import uuid
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#   USER_TYPE_CHOICES = (
#       (1, 'student'),
#       (2, 'teacher'),
#       (3, 'secretary'),
#       (4, 'supervisor'),
#       (5, 'admin'),
#   )

#   user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

# class GEO_TAGGING(models.Model):
#     district = models.CharField(max_length=15,default="",null=True)
#     city = models.CharField(max_length=15,default="",null=True)
#     annuxure_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
#     dpr_no = models.IntegerField(null=True)
#     balance = models.IntegerField(null=True)
#     date = models.DateField(null=True)

#     class Meta:
#      permissions = (
#            ("view_records", "Can view records"),
#      )

#     def __str__(self):
#         return str(self.annuxure_id)

# class FUND_DETAILS(models.Model):
#     fn = models.IntegerField(null=True)
#     sn = models.IntegerField(null=True)
#     tn = models.IntegerField(null=True)
#     fu = models.IntegerField(null=True)
#     su = models.IntegerField(null=True)
#     tu = models.IntegerField(null=True)
#     user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
#     fund_id = models.AutoField(primary_key=True)

#     def __str__(self):
#         return str(self.fund_id)
class Admin(models.Model):
    name = models.CharField(max_length=15,default="",null=True)
    phonenumber = models.CharField(max_length=10,default="",null=True)
    address = models.CharField(max_length=15,default="",null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    class Meta:
     permissions = (
           ("is_admin", "Can view records"),
     )

    def __str__(self):
        return str(self.name)
class Student(models.Model):
    name = models.CharField(max_length=15,default="",null=True)
    usn = models.CharField(max_length=15,default="",null=True)
    phonenumber = models.CharField(max_length=10,default="",null=True)
    address = models.CharField(max_length=15,default="",null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)


class Teachers(models.Model):
    name = models.CharField(max_length=15,default="",null=True)
    phonenumber = models.CharField(max_length=10,default="",null=True)
    address = models.CharField(max_length=15,default="",null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    class Meta:
     permissions = (
           ("is_teacher", "can view marks"),
     )

    def __str__(self):
        return str(self.name)


class Img(models.Model): 
    coursename = models.CharField(max_length=50) 
    description = models.CharField(max_length=1000)
    platform = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.coursename)

 
 
class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y')
    description = models.CharField(max_length=1000,default=None)
    user = models.ForeignKey(Img, default=None, on_delete=models.CASCADE)
     
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.title

class Enroll(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    img = models.ForeignKey(Img, default=None, on_delete=models.CASCADE)


class Exam(models.Model): 
    examname = models.CharField(max_length=50) 
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.examname)

class Quiz(models.Model):
    question = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100,default="",null=True)
    op4 = models.CharField(max_length=100,default="",null=True)
    answer = models.CharField(max_length=1000,default=None)
    user = models.ForeignKey(Exam, default=None, on_delete=models.CASCADE)
     
    class Meta:
        verbose_name = 'quiz'
        verbose_name_plural = 'quizzes'
         
    def __str__(self):
        return self.question

class Results(models.Model):
    result = models.BooleanField(default=None)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    img = models.ForeignKey(Exam, default=None, on_delete=models.CASCADE)

class Profile(models.Model):
    description = models.CharField(max_length=1000,default=None,null=True)
    website = models.CharField(max_length=1000,default=None,null=True)
    role = models.CharField(max_length=100,default=None,null=True)
    image = models.ImageField(upload_to='images/',null=True)


    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)



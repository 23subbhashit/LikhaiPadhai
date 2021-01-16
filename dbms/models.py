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
    phonenumber = models.IntegerField(null=True)
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
    phonenumber = models.IntegerField(null=True)
    address = models.CharField(max_length=15,default="",null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)


class Teachers(models.Model):
    name = models.CharField(max_length=15,default="",null=True)
    phonenumber = models.IntegerField(null=True)
    address = models.CharField(max_length=15,default="",null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    class Meta:
     permissions = (
           ("is_teacher", "can view marks"),
     )

    def __str__(self):
        return str(self.name)
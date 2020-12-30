from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class GEO_TAGGING(models.Model):
    district = models.CharField(max_length=15,default="",null=True)
    city = models.CharField(max_length=15,default="",null=True)
    annuxure_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    dpr_no = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return str(self.annuxure_id)

class FUND_DETAILS(models.Model):
    fn = models.IntegerField(null=True)
    sn = models.IntegerField(null=True)
    tn = models.IntegerField(null=True)
    fu = models.IntegerField(null=True)
    su = models.IntegerField(null=True)
    tu = models.IntegerField(null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    fund_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.fund_id)
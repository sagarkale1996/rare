from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class exuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    mob_no=models.IntegerField()
    address=models.CharField(max_length=120)


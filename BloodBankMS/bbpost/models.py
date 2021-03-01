from django.db import models
from django.contrib.auth.models import User

class BloodClass(models.Model):
    blood_group1 = models.CharField(max_length=3)
    age1 = models.IntegerField()
    #dtime = 
    address1 = models.CharField(max_length=250)
    phone_number1 = models.CharField(max_length=14)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




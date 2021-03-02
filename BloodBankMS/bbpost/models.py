from django.db import models
from django.contrib.auth.models import User

class BloodClass2(models.Model):
    blood_group = models.CharField(max_length=3)
    age = models.IntegerField()
    ctime= models.DateTimeField(auto_now_add=True)
    dtime = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=14)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(blank=True) 

    def __str__(self):
        return self.phone_number




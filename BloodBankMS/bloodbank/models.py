from django.db import models
from django.contrib.auth.models import User

class BloodClass(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3)
    age = models.IntegerField()
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=14)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




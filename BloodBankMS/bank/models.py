from django.db import models

# Create your models here.
class BloodClass3(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=14)


    def __str__(self):
        return self.name

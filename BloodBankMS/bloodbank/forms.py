from django.forms import ModelForm
from .models import BloodClass

class BloodForm(ModelForm):
    class Meta:
        model = BloodClass
        fields = ('name', 'age', 'blood_group','address','phone_number')

#All models name:
    # name = models.CharField(max_length=100)
    # blood_group = models.CharField(max_length=3)
    # age = models.IntegerField()
    # address = models.CharField(max_length=250)
    # phone_number = models.CharField(max_length=14)

    # user = models.ForeignKey(User,on_delete=models.CASCADE)

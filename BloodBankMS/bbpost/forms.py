from django.forms import ModelForm
from .models import BloodClass2

class BloodForm2(ModelForm):
    class Meta:
        model = BloodClass2
        fields = ('blood_group', 'age', 'address','phone_number','comment')
        
#all model class
    # blood_group = models.CharField(max_length=3)
    # age = models.IntegerField()
    # ctime= models.DateTimeField(auto_now_add=True)
    # dtime = models.DateTimeField(blank=True, null=True)
    # address = models.CharField(max_length=250)
    # phone_number = models.CharField(max_length=14)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

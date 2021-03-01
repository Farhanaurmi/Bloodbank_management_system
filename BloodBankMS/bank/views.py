from django.shortcuts import render
from .models import BloodClass3

# Create your views here.
def bloodbank(request):
    bbform = BloodClass3.objects.all()
    return render(request, 'bank/bloodbank.html', {'bbform':bbform})
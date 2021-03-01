from django.shortcuts import render

# Create your views here.

def bbpost_home(request):
    return render(request, 'bbpost/phome.html')

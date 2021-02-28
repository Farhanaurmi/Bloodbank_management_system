from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'bloodbank/home.html')

def signupuser(request):
    if request.method=='GET':
        return render(request, 'bloodbank/signupuser.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'bloodbank/signupuser.html', {'form':UserCreationForm,'error':'username has been already taken'})
        else:
            return render(request, 'bloodbank/signupuser.html', {'form':UserCreationForm,'error':'password did not match'})
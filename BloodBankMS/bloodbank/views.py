from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import BloodClass


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


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'bloodbank/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'bloodbank/login.html', {'form':AuthenticationForm(), 'error':'Error! Try again with correct username & password'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def donoruser(request):
    form = BloodClass.objects.all()
    return render(request,'bloodbank/donor.html', {'form':form})

@login_required
def donordetails(request,donor_id):
    dd = get_object_or_404(BloodClass, pk=donor_id)
    return render(request,'bloodbank/donordetails.html', {'dd':dd})


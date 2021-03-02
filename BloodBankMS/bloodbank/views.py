from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import BloodClass
from .forms import BloodForm


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

@login_required
def donorreg(request):
    if request.method == 'GET':
        return render(request, 'bloodbank/donorreg.html', {'form':BloodForm()})
    else:
        try:
            dr = BloodForm(request.POST)
            new_dr = dr.save(commit=False)
            new_dr.user = request.user
            new_dr.save()
            return redirect('donoruser')

        except ValueError:
            return render(request, 'bloodbank/donorreg.html', {'form':BloodForm(), 'error':'Error! Try again!'})

@login_required
def mdprofile(request):
    form = BloodClass.objects.filter(user= request.user)
    return render(request,'bloodbank/myprofile.html', {'form':form})

@login_required
def dedit(request, d_pk):
    obj = get_object_or_404(BloodClass, pk=d_pk,user=request.user)
    if request.method=='GET':
        dform=BloodForm(instance=obj)
        return render(request,'bloodbank/edit.html',{'dform':dform,'obj':obj})
    else:
        try:
            dform = BloodForm(request.POST,instance=obj)
            dform.save()
            return redirect('mdprofile')
        except ValueError:
            return render(request,'bloodbank/edit.html',{'dform':dform,'obj':obj,'error':'Error! Try again'} )



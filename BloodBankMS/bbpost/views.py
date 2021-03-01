from django.shortcuts import render, redirect
from .models import BloodClass2
from .forms import BloodForm2
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def bbpost_home(request):
    form = BloodClass2.objects.all()
    return render(request,'bbpost/phome.html', {'form':form})


@login_required
def cpost(request):
    if request.method == 'GET':
        return render(request, 'bbpost/rpost.html', {'form':BloodForm2()})
    else:
        try:
            dr = BloodForm2(request.POST)
            new_dr = dr.save(commit=False)
            new_dr.user = request.user
            new_dr.save()
            return redirect('bbpost_home')
        except ValueError:
            return render(request, 'bbpost/rpost.html', {'form':BloodForm2(), 'error':'Error! Try again!'})
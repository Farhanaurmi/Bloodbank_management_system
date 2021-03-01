from django.shortcuts import render, redirect, get_object_or_404
from .models import BloodClass2
from .forms import BloodForm2
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.

@login_required
def bbpost_home(request):
    form = BloodClass2.objects.all()
    return render(request,'bbpost/phome.html', {'form':form})


@login_required
def cpost(request):
    if request.method == 'GET':
        return render(request, 'bbpost/cpost.html', {'form':BloodForm2()})
    else:
        try:
            dr = BloodForm2(request.POST)
            new_dr = dr.save(commit=False)
            new_dr.user = request.user
            new_dr.save()
            return redirect('bbpost_home')
        except ValueError:
            return render(request, 'bbpost/cpost.html', {'form':BloodForm2(), 'error':'Error! Try again!'})

@login_required
def dpost(request,d_id):
    dd2 = get_object_or_404(BloodClass2, pk=d_id)
    return render(request,'bbpost/dpost.html', {'dd':dd2})

@login_required
def mypostd(request,m_id):
    dd2 = get_object_or_404(BloodClass2, pk=m_id, user=request.user)
    return render(request,'bbpost/mypostd.html', {'dd':dd2})

@login_required
def mypost(request):
    form = BloodClass2.objects.filter(user=request.user, dtime__isnull=True)
    return render(request, 'bbpost/mypost.html', {'form':form})
    
@login_required
def mypostdelete(request,m_id):
    dd2 = get_object_or_404(BloodClass2, pk=m_id, user=request.user)
    if request.method == 'POST':
        dd2.dtime = timezone.now()
        dd2.delete()
        return redirect('mypost')


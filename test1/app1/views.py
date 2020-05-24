from django.shortcuts import render,redirect
from .models import Emp
from .forms import EmpForm,SignUpForm

# Create your views here.
def baseview(request):
    return render(request,'app1/base.html')

def homeview(request):
    emp=Emp.objects.all()
    return render(request,'app1/home.html',{'emp':emp})

def addview(request):
    form=EmpForm()
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'app1/add.html',{'form':form})
def deleteview(request,id):
    emp=Emp.objects.get(id=id)
    emp.delete()
    return redirect('/home')

def updateview(request,id):
    emp=Emp.objects.get(id=id)
    form=EmpForm(instance=emp)
    if request.method=="POST":
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'app1/update.html',{'form':form})

def signupview(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login')
    return render(request,'app1/signup.html',{'form':form})

def logoutview(request):
    return render(request,'app1/logout.html')




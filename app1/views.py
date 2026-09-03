import math
from django.shortcuts import render
from app1.forms import *

h=6.626e-34
c=3e8
g=9.8

def home(request):     
    return render(request,'app1/index.html')

def calc_final_velocity1(u,a,s):
    return math.sqrt(u**2+(2*a*s))

def calc_final_velocity2(u,a,t):
    return u+a*t

def calc_displacement(u,a,t):
    return u*t+0.5*a*(t**2)

def energy_calc(lambda1):
    return (h*c)/lambda1;

def calc_time_flight(theta,u):   
    theta_radian=math.radians(theta)
    return (2*u*(math.sin(theta_radian)))/g
    
def calc_max_height(theta,u):    
    theta_radian=math.radians(theta)   
    return (u**2*(math.sin(theta_radian))**2)/(2*g)

def calc_horizontal_range(theta,u):
    theta_radian=math.radians(theta)
    return (u**2*(math.sin(2*theta_radian)))/g

#v^2=u^2+2as
def final_velocity1(request):
    if request.method=='POST':
        form1=PhysicsForm(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            a=data.get('a')
            s=data.get('s')
            result=calc_final_velocity1(u,a,s)
            return render(request,'app1/formula.html',{'param1':result,'form':form1})
    else: form1=PhysicsForm() 
    return render(request,'app1/formula.html',{'form':form1})  

#v=u+at
def final_velocity2(request):
    if request.method=='POST':
        form1=PhysicsForm1(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            a=data.get('a')
            t=data.get('t')
            result=calc_final_velocity2(u,a,t)
            return render(request,'app1/formula1.html',{'param2':result,'form':form1})
    else: form1=PhysicsForm1() 
    return render(request,'app1/formula1.html',{'form':form1})  

def displacement(request):
    if request.method=='POST':
            form1=PhysicsForm1(request.POST)
            if form1.is_valid():
                data = form1.cleaned_data
                u=data.get('u')
                a=data.get('a')
                t=data.get('t')
                result=calc_displacement(u,a,t)
                return render(request,'app1/formula2.html',{'param2':result,'form':form1})
    else: form1=PhysicsForm1() 
    return render(request,'app1/formula2.html',{'form':form1})  

def energy_atom(request):
    if request.method=='POST':
        form1=PhysicsForm2(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            lambda1=data.get('lambda1')
            result=energy_calc(lambda1)
            return render(request,'app1/formula3.html',{'param2':result,'form':form1})
    else: form1=PhysicsForm2() 
    return render(request,'app1/formula3.html',{'form':form1})  

def time_flight(request):
    if request.method=='POST':
            form1=PhysicsForm3(request.POST)
            if form1.is_valid():
                data = form1.cleaned_data
                u=data.get('u')
                theta=data.get('theta')
                result=calc_time_flight(theta,u)
                return render(request,'app1/formula4.html',{'param2':result,'form':form1})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formula4.html',{'form':form1}) 

def max_height(request):
    if request.method=='POST':
        form1=PhysicsForm3(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            theta=data.get('theta')
            result=calc_max_height(theta,u)
            return render(request,'app1/formula5.html',{'param2':result,'form':form1})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formula5.html',{'form':form1})

def horizontal_range(request):
    if request.method=='POST':
        form1=PhysicsForm3(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            theta=data.get('theta')
            result=calc_horizontal_range(theta,u)
            return render(request,'app1/formula6.html',{'param2':result,'form':form1})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formula6.html',{'form':form1})
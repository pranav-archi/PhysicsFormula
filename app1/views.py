import math
from django.shortcuts import render
from app1.forms import PhysicsForm
# Create your views here.
from django.http import HttpResponse
def home(request):
    if request.method=='POST':
        form1=PhysicsForm(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            a=data.get('a')
            s=data.get('s')
            result=calc_final_velocity1(u,a,s)
            return render(request,'app1/index.html',{'param1':result,'form':form1})
    else: form1=PhysicsForm()       
    return render(request,'app1/index.html',{'form':form1})

def calc_final_velocity1():
    #return math.sqrt(u**2+(2*a*s))
    return HttpResponse('Final velocity')

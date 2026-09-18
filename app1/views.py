import math
from django.shortcuts import render
from app1.forms import *

h=6.626e-34
c=3e8
g=9.8
epsilon0=8.854e-12

def home(request):     
    return render(request,'app1/index.html')

def calc_final_velocity1(u,a,s):
    return math.sqrt(u**2+(2*a*s))

def calc_final_velocity2(u,a,t):
    v=u+a*t
    return v

def calc_displacement(u,a,t):
    s=u*t+0.5*a*(t**2)
    return s

def energy_calc(lambda1):
    energy=(h*c)/lambda1
    return energy

def calc_time_flight(theta,u):   
    theta_radian=math.radians(theta)
    T_f=(2*u*(math.sin(theta_radian)))/g
    return T_f
    
def calc_max_height(theta,u):    
    theta_radian=math.radians(theta)
    H=(u**2*(math.sin(theta_radian))**2)/(2*g)
    return H

def calc_horizontal_range(theta,u):
    theta_radian=math.radians(theta)
    R=(u**2*(math.sin(2*theta_radian)))/g
    return R

def calc_parallel_plate_capacitance(K,A,d):
    capacitance_par_plate=(K*epsilon0*A)/d
    return capacitance_par_plate

def calc_half_life(decay_const):
    t_half=math.log(2)/decay_const
    return t_half

def calc_kinetic_energy(m,v):
    kin_energy=0.5*m*(v**2)
    return kin_energy

def calc_cap_potential_energy(C,V):
    U_c=0.5*C*(V**2)
    return U_c
    
def calc_grav_potential_energy(m,h):
    U_g=m*g*h
    return U_g
    
def calc_voltage(I,R):
    V=I*R
    return V

def calc_incident_angle(theta1,n1,n2):
    theta_radian=math.sin(math.radians(theta1))
    theta2=math.asin((n1*theta_radian)/n2)
    return math.degrees(theta2)

def calc_emf_conductor(B,l,v):
    emf=B*l*v
    return emf

def final_velocity1(request):
    if request.method=='POST':
        form1=PhysicsForm(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            a=data.get('a')
            s=data.get('s')
            result=calc_final_velocity1(u,a,s)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'1st Kinematic Equation(v2=u2+2as)','formula':'final_velocity1'})
    else: form1=PhysicsForm() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'1st Kinematic Equation(v2=u2+2as)','formula':'final_velocity1'})  

    
def final_velocity2(request):
    if request.method=='POST':
        form1=PhysicsForm1(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            a=data.get('a')
            t=data.get('t')
            result=calc_final_velocity2(u,a,t)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'2nd Kinematic Equation(v=u+at)','formula':'final_velocity2'})
    else: form1=PhysicsForm1() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'2nd Kinematic Equation(v=u+at)','formula':'final_velocity2'})  

def displacement(request):
    if request.method=='POST':
            form1=PhysicsForm1(request.POST)
            if form1.is_valid():
                data = form1.cleaned_data
                u=data.get('u')
                a=data.get('a')
                t=data.get('t')
                result=calc_displacement(u,a,t)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'3rd Kinematic Equation(s=ut+1/2at^2)','formula':'displacement'})
    else: form1=PhysicsForm1() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'3rd Kinematic Equation(s=ut+1/2at2)','formula':'displacement'})  

def energy_light(request):
    if request.method=='POST':
        form1=PhysicsForm2(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            lambda1=data.get('lambda1')
            result=energy_calc(lambda1)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Energy of a light','formula':'energy_light'})
    else: form1=PhysicsForm2() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Energy of a light','formula':'energy_light'})  

def time_flight(request):
    if request.method=='POST':
            form1=PhysicsForm3(request.POST)
            if form1.is_valid():
                data = form1.cleaned_data
                u=data.get('u')
                theta=data.get('theta')
                result=calc_time_flight(theta,u)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Time of flight of a Projectile','formula':'time_flight'})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Time of flight of a Projectile','formula':'time_flight'}) 

def max_height(request):
    if request.method=='POST':
        form1=PhysicsForm3(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            theta=data.get('theta')
            result=calc_max_height(theta,u)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Maximum height of an Object in a Projectile','formula':'max_height'})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Maximum height of an Object in a Projectile','formula':'max_height'})

def horizontal_range(request):
    if request.method=='POST':
        form1=PhysicsForm3(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            theta=data.get('theta')
            result=calc_horizontal_range(theta,u)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Horizontal Range of an Object in a Projectile','formula':'horizontal_range'})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Horizontal Range of an Object in a Projectile','formula':'horizontal_range'})

def parallel_plate_capacitance(request):
    if request.method=='POST':
        form1= PhysicsForm4(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            K=data.get('K')
            A=data.get('A')
            d=data.get('d')
            result=calc_parallel_plate_capacitance(K,A,d)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Capacitance of Parallel Plate Capacitor','formula':'par_plate_capacitance'})
    else: form1=PhysicsForm4() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Capacitance of Parallel Plate Capacitor','formula':'par_plate_capacitance'})
            
def half_life(request):
    if request.method=='POST':
        form1= PhysicsForm5(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            decay_const=data.get('decay_const')
            result=calc_half_life(decay_const)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Half life of nuclear atom','formula':'half_life'})
    else: form1=PhysicsForm5()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Half life of nuclear atom','formula':'half_life'}) 

def kinetic_energy(request):
    if request.method=='POST':
        form1= PhysicsForm6(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            m=data.get('m')
            v=data.get('v')
            result=calc_kinetic_energy(m,v)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Kinetic Energy','formula':'kinetic_energy'})
    else: form1=PhysicsForm6()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Kinetic Energy','formula':'kinetic_energy'}) 

def capacitor_pot_energy(request):
    if request.method=='POST':
        form1=PhysicsForm7(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            C=data.get('C')
            V=data.get('V')
            result=calc_cap_potential_energy(C,V)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Potential energy of a Capacitor','formula':'capacitor_pot_energy'})
    else: form1=PhysicsForm7()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Potential energy of a Capacitor','formula':'capacitor_pot_energy'})

def grav_pot_energy(request):
    if request.method=='POST':
        form1=PhysicsForm8(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            m=data.get('m')
            h=data.get('h')
            result=calc_grav_potential_energy(m,h)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Gravitational Potential energy','formula':'gravitational_pot_energy'})
    else: form1=PhysicsForm8()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Potential energy of a Capacitor','formula':'capacitor_pot_energy'})

def ohm_law(request):
    if request.method=='POST':
        form1=PhysicsForm9(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            I=data.get('I')
            R=data.get('R')
            result=calc_voltage(I,R)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Ohm's Law",'formula':'ohm_law'})
    else: form1=PhysicsForm9()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Ohm's Law",'formula':'ohm_law'})

def snell_law(request):
    if request.method=='POST':
        form1=PhysicsForm10(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            theta1=data.get('theta1')
            n1=data.get('n1')
            n2=data.get('n2')
            result=calc_incident_angle(theta1,n1,n2)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Snell's Law",'formula':'snell_law'})
    else: form1=PhysicsForm10()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Snell's Law",'formula':'snell_law'})

def emf_wire(request):
    if request.method=='POST':
            form1=PhysicsForm11(request.POST)
            if form1.is_valid():
                data=form1.cleaned_data
                B=data.get('B')
                l=data.get('l')
                v=data.get('v')
                result=calc_emf_conductor(B,l,v)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"EMF of a conductor",'formula':'emf_conductor'})
    else: form1=PhysicsForm11()
    return render(request,'app1/formulas.html',{'form':form1,'title':"EMF of a conductor",'formula':'emf_conductor'})
    
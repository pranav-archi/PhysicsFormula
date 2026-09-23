import math
from django.shortcuts import render
from app1.forms import *

G=6.674e-11
h=6.626e-34
c=3e8
g=9.8
epsilon0=8.854e-12
k_coulomb=8.99e9

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

def calc_elec_force(q1,q2,r):
    F_e= (k_coulomb*q1*q2)/(r**2)
    return F_e

def calc_grav_force(q1,q2,r):
    F_g= (G*q1*q2)/(r**2)
    return F_g

def calc_centripetal_force(m,v,r):
    F_c=(m*(v**2))/r
    return F_c

def calc_focal_length(d_i,d_o):
    f=1/((1/d_i)+(1/d_o))
    return f

def calc_energy_atom(m):
    E=m*(c**2)
    return E

def calc_resistivity(R,A,l):
    rho=(R*A)/l
    return rho

def calc_rotational_kin_energy(I,omega):
    K_rot=0.5*I*(omega**2)
    return K_rot

def calc_net_work(K_f,K_i):
    net_work=K_f-K_i
    return net_work

def calc_net_internal_energy(Q,W):
    del_U=Q-W
    return del_U

def calc_photon_momentum(lambda1):
    p=h/lambda1
    return p

def calc_impedance_lcr(R,X_C,X_L):
    Z=math.sqrt((R**2)+((X_C-X_L)**2))
    return Z

def calc_resonant_frequency(L,C):
    f_r=1/(2*math.pi*math.sqrt(L*C))
    return f_r

def calc_newton_force(m,a):
    F_newton=m*a
    return F_newton

def calc_nuclei_left(N_0,decay_const,t):
    N_t=N_0*(math.exp(-decay_const*t))
    return N_t

def final_velocity1(request):
    if request.method=='POST':
        form1=PhysicsForm(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            a=data.get('a')
            s=data.get('s')
            result=calc_final_velocity1(u,a,s)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'1st Kinematic Equation(v2=u2+2as)'})
    else: form1=PhysicsForm() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'1st Kinematic Equation(v2=u2+2as)'})  

    
def final_velocity2(request):
    if request.method=='POST':
        form1=PhysicsForm1(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            a=data.get('a')
            t=data.get('t')
            result=calc_final_velocity2(u,a,t)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'2nd Kinematic Equation(v=u+at)'})
    else: form1=PhysicsForm1() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'2nd Kinematic Equation(v=u+at)'})  

def displacement(request):
    if request.method=='POST':
            form1=PhysicsForm1(request.POST)
            if form1.is_valid():
                data = form1.cleaned_data
                u=data.get('u')
                a=data.get('a')
                t=data.get('t')
                result=calc_displacement(u,a,t)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'3rd Kinematic Equation(s=ut+1/2at^2)'})
    else: form1=PhysicsForm1() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'3rd Kinematic Equation(s=ut+1/2at2)'})  

def energy_light(request):
    if request.method=='POST':
        form1=PhysicsForm2(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            lambda1=data.get('lambda1')
            result=energy_calc(lambda1)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Energy of a light'})
    else: form1=PhysicsForm2() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Energy of a light'})  

def time_flight(request):
    if request.method=='POST':
            form1=PhysicsForm3(request.POST)
            if form1.is_valid():
                data = form1.cleaned_data
                u=data.get('u')
                theta=data.get('theta')
                result=calc_time_flight(theta,u)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Time of flight of a Projectile'})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Time of flight of a Projectile'}) 

def max_height(request):
    if request.method=='POST':
        form1=PhysicsForm3(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            theta=data.get('theta')
            result=calc_max_height(theta,u)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Maximum height of an Object in a Projectile'})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Maximum height of an Object in a Projectile'})

def horizontal_range(request):
    if request.method=='POST':
        form1=PhysicsForm3(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            u=data.get('u')
            theta=data.get('theta')
            result=calc_horizontal_range(theta,u)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Horizontal Range of an Object in a Projectile'})
    else: form1=PhysicsForm3() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Horizontal Range of an Object in a Projectile'})

def parallel_plate_capacitance(request):
    if request.method=='POST':
        form1= PhysicsForm4(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            K=data.get('K')
            A=data.get('A')
            d=data.get('d')
            result=calc_parallel_plate_capacitance(K,A,d)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Capacitance of Parallel Plate Capacitor'})
    else: form1=PhysicsForm4() 
    return render(request,'app1/formulas.html',{'form':form1,'title':'Capacitance of Parallel Plate Capacitor'})
            
def half_life(request):
    if request.method=='POST':
        form1= PhysicsForm5(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            decay_const=data.get('decay_const')
            result=calc_half_life(decay_const)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Half life of nuclear atom'})
    else: form1=PhysicsForm5()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Half life of nuclear atom'}) 

def kinetic_energy(request):
    if request.method=='POST':
        form1= PhysicsForm6(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            m=data.get('m')
            v=data.get('v')
            result=calc_kinetic_energy(m,v)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Kinetic Energy'})
    else: form1=PhysicsForm6()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Kinetic Energy'}) 

def capacitor_pot_energy(request):
    if request.method=='POST':
        form1=PhysicsForm7(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            C=data.get('C')
            V=data.get('V')
            result=calc_cap_potential_energy(C,V)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Potential energy of a Capacitor'})
    else: form1=PhysicsForm7()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Potential energy of a Capacitor'})

def grav_pot_energy(request):
    if request.method=='POST':
        form1=PhysicsForm8(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            m=data.get('m')
            h=data.get('h')
            result=calc_grav_potential_energy(m,h)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':'Gravitational Potential energy'})
    else: form1=PhysicsForm8()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Potential energy of a Capacitor'})

def ohm_law(request):
    if request.method=='POST':
        form1=PhysicsForm9(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            I=data.get('I')
            R=data.get('R')
            result=calc_voltage(I,R)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Ohm's Law"})
    else: form1=PhysicsForm9()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Ohm's Law"})

def snell_law(request):
    if request.method=='POST':
        form1=PhysicsForm10(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            theta1=data.get('theta1')
            n1=data.get('n1')
            n2=data.get('n2')
            result=calc_incident_angle(theta1,n1,n2)
            return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Snell's Law"})
    else: form1=PhysicsForm10()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Snell's Law"})

def emf_wire(request):
    if request.method=='POST':
            form1=PhysicsForm11(request.POST)
            if form1.is_valid():
                data=form1.cleaned_data
                B=data.get('B')
                l=data.get('l')
                v=data.get('v')
                result=calc_emf_conductor(B,l,v)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"EMF of a conductor"})
    else: form1=PhysicsForm11()
    return render(request,'app1/formulas.html',{'form':form1,'title':"EMF of a conductor"})

def coulomb_law(request):
    if request.method=='POST':
        form1= PhysicsForm12(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                q1=data.get('q1')
                q2=data.get('q2')
                r=data.get('r')
                result=calc_elec_force(q1,q2,r)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Coulomb's Law"})
    else: form1=PhysicsForm12()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Coulomb's Law"})

def gravitational_law(request):
    if request.method=='POST':
        form1= PhysicsForm13(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                m1=data.get('m1')
                m2=data.get('m2')
                r=data.get('r')
                result=calc_grav_force(m1,m2,r)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Gravitational Law"})
    else: form1=PhysicsForm13()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Gravitational Law"})

def centripetal_force(request):
    if request.method=='POST':
        form1= PhysicsForm14(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                m=data.get('m')
                v=data.get('v')
                r=data.get('r')
                result=calc_centripetal_force(m,v,r)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Centripetal Force"})
    else: form1=PhysicsForm14()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Centripetal Force"})

def thin_lens_eq(request):
    if request.method=='POST':
        form1= PhysicsForm15(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                d_i=data.get('d_i')
                d_o=data.get('d_o')
                result=calc_focal_length(d_i,d_o)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Thin Lens Equation"})
    else: form1=PhysicsForm15()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Thin Lens Equation"})

def einstein_eq(request):
    if request.method=='POST':
            form1= PhysicsForm16(request.POST)
            if form1.is_valid():
                    data=form1.cleaned_data
                    m=data.get('m')
                    result=calc_energy_atom(m)
                    return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Einstein's Energy Equation"})
    else: form1=PhysicsForm16()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Einstein's Energy Equation"})

def resistivity(request):
    if request.method=='POST':
        form1= PhysicsForm17(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                R=data.get('R')
                A=data.get('A')
                l=data.get('l')
                result=calc_resistivity(R,A,l)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Resistivity of a Conductor"})
    else: form1=PhysicsForm17()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Resistivity of a Conductor"})

def rot_kinetic_energy(request):
    if request.method=='POST':
        form1= PhysicsForm18(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                I=data.get('I')
                omega=data.get('omega')
                result=calc_rotational_kin_energy(I,omega)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Rotational Kinetic Energy"})
    else: form1=PhysicsForm18()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Rotational Kinetic Energy'})

def work_energy_theorem(request):
    if request.method=='POST':
            form1= PhysicsForm19(request.POST)
            if form1.is_valid():
                    data=form1.cleaned_data
                    K_f=data.get('K_f')
                    K_i=data.get('K_i')
                    result=calc_net_work(K_f,K_i)
                    return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Work Energy Theorem"})
    else: form1=PhysicsForm19()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Work Energy Theorem'})

def net_internal_energy(request):
    if request.method=='POST':
            form1= PhysicsForm20(request.POST)
            if form1.is_valid():
                    data=form1.cleaned_data
                    Q=data.get('Q')
                    W=data.get('W')
                    result=calc_net_internal_energy(Q,W)
                    return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Work Energy Theorem"})
    else: form1=PhysicsForm20()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Work Energy Theorem'})

def photon_momentum(request):
    if request.method=='POST':
            form1= PhysicsForm2(request.POST)
            if form1.is_valid():
                    data=form1.cleaned_data
                    lambda1=data.get('lambda1')
                    result=calc_photon_momentum(lambda1)
                    return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Photon Momentum"})
    else: form1=PhysicsForm2()
    return render(request,'app1/formulas.html',{'form':form1,'title':'Photon momentum'})

def impedance_lcr(request):
    if request.method=='POST':
        form1= PhysicsForm21(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                R=data.get('R')
                X_C=data.get('X_C')
                X_L=data.get('X_L')
                result=calc_impedance_lcr(R,X_C,X_L)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Impedance of LCR Circuit"})
    else: form1=PhysicsForm21()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Impedance of LCR Circuit"})

def resonant_frequency(request):
    if request.method=='POST':
        form1= PhysicsForm22(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                L=data.get('L')
                C=data.get('C')
                result=calc_resonant_frequency(L,C)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Impedance of LCR Circuit"})
    else: form1=PhysicsForm22()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Impedance of LCR Circuit"})

def newton_force(request):
    if request.method=='POST':
        form1= PhysicsForm23(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                m=data.get('m')
                a=data.get('a')
                result=calc_newton_force(m,a)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Newton's 2nd Law of Motion"})
    else: form1=PhysicsForm23()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Newton's Law of Gravitation"})

def radioactivity_law(request):
    if request.method=='POST':
        form1= PhysicsForm24(request.POST)
        if form1.is_valid():
                data=form1.cleaned_data
                N_0=data.get('N_0')
                decay_const=data.get('decay_const')
                t=data.get('t')
                result=calc_nuclei_left(N_0,decay_const,t)
                return render(request,'app1/formulas.html',{'param2':result,'form':form1,'title':"Radioactivity Decay Law"})
    else: form1=PhysicsForm24()
    return render(request,'app1/formulas.html',{'form':form1,'title':"Radioactivity Decay Law"})
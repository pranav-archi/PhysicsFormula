from django import forms

class PhysicsForm(forms.Form):
    u=forms.IntegerField(label='Enter initial velocity:')
    a=forms.IntegerField(label='Enter acceleration:')
    s=forms.IntegerField(label='Enter displacement:')

class PhysicsForm1(forms.Form):
    u=forms.IntegerField(label='Enter initial velocity:')
    a=forms.IntegerField(label='Enter acceleration:')
    t=forms.IntegerField(label='Enter time:')

class PhysicsForm2(forms.Form):
    lambda1=forms.FloatField(label='Enter wavelength:')

class PhysicsForm3(forms.Form):
    u=forms.IntegerField(label='Enter initial velocity:')
    theta=forms.IntegerField(label='Enter the projection angle:')
    
class PhysicsForm4(forms.Form):
    K=forms.FloatField(label='Enter dielectric constant:')
    A=forms.FloatField(label='Enter the area of capacitor:')
    d=forms.FloatField(label='Enter the distance between the two capacitors:')

class PhysicsForm5(forms.Form):
    decay_const=forms.FloatField(label='Enter the decay constant:')
    
class PhysicsForm6(forms.Form):
    m=forms.IntegerField(label='Enter the mass:')
    v=forms.IntegerField(label='Enter the velocity:')

class PhysicsForm7(forms.Form):
    C=forms.FloatField(label="Enter the capacitance:")
    V=forms.FloatField(label="Enter the voltage:")
    
class PhysicsForm8(forms.Form):
    m=forms.IntegerField(label="Enter the mass:")
    h=forms.IntegerField(label="Enter the height:")
    
class PhysicsForm9(forms.Form):
    I=forms.FloatField(label='Enter the electric current:')
    R=forms.FloatField(label='Enter the resistance:')
    
class PhysicsForm10(forms.Form):
    theta1=forms.IntegerField(label='Enter the incident angle for medium 1:',required=False)
    n1=forms.FloatField(label='Enter the refractive index of medium 1:')
    n2=forms.FloatField(label='Enter the refractive index of medium 2:')
    
class PhysicsForm11(forms.Form):
    B=forms.FloatField(label='Enter the magnetic field strength:')
    l=forms.FloatField(label='Enter the length of the wire:')
    v=forms.FloatField(label='Enter the velocity:')

class PhysicsForm12(forms.Form):
    q1=forms.FloatField(label='Enter the charge of first atom:')
    q2=forms.FloatField(label='Enter the charge of second atom:')
    r=forms.FloatField(label='Enter the distance between two atoms:')

class PhysicsForm13(forms.Form):
    m1=forms.FloatField(label='Enter the mass of first object:')
    m2=forms.FloatField(label='Enter the mass of second object:')
    r=forms.FloatField(label='Enter the distance between two objects:')
    
class PhysicsForm14(forms.Form):
    m=forms.IntegerField(label='Enter the mass:')
    v=forms.IntegerField(label='Enter the velocity:')
    r=forms.IntegerField(label='Enter the radius:')
    
class PhysicsForm15(forms.Form):
    d_i=forms.IntegerField(label='Enter the image distance:')
    d_o=forms.IntegerField(label='Enter the object distance:')
    
class PhysicsForm16(forms.Form):
    m=forms.IntegerField(label='Enter the mass:')
    
class PhysicsForm17(forms.Form):
    R=forms.FloatField(label='Enter the resistance:')
    A=forms.FloatField(label='Enter the area:')
    l=forms.FloatField(label='Enter the length:')

class PhysicsForm18(forms.Form):
    I=forms.IntegerField(label='Enter the inertia:')
    omega=forms.IntegerField(label='Enter the angular velocity:')
    
class PhysicsForm19(forms.Form):
    K_f=forms.FloatField(label='Enter the final kinetic energy:')
    K_i=forms.FloatField(label='Enter the initial kinetic energy:')

class PhysicsForm20(forms.Form):
    Q=forms.FloatField(label='Enter the net heat transfered:')
    W=forms.FloatField(label='Enter the net work done:')
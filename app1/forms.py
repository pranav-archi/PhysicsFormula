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
    
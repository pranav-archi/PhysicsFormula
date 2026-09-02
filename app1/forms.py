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
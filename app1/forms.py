from django import forms

class PhysicsForm(forms.Form):
    u=forms.IntegerField(label='Enter initial velocity:')
    a=forms.IntegerField(label='Enter acceleration:')
    s=forms.IntegerField(label='Enter time:')
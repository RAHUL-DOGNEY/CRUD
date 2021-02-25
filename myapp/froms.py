from django import forms
# from django.core import validators
from .models import Users

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email','pwd']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'pwd': forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            
    }

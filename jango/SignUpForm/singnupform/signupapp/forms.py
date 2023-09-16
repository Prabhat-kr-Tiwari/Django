# appname/forms.py
from django import forms
from .models import UserData

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'email', 'address', 'pincode', 'phone_no', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from phonenumber_field.modelfields import PhoneNumberField
from .models import Account

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())
    PhoneNumber =PhoneNumberField(blank=True)

    class Meta:
        model=Account
        fields = ('username','email','password1','password2','PhoneNumber')
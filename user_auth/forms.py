from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full Name","class":"form-control sign_up_form_group"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email","class":"form-control"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","class":"form-control"}))
    class Meta:
        model= User
        fields=['username','email']

class UserUpdateForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full Name","class":"form-control sign_up_form_group"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email","class":"form-control"}))
    class Meta:
        model=User
        fields=['username','email']    

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control mb-3"}))
    class Meta:
        model=Profile
        fields=['image']

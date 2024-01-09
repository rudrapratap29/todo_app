from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'passwrod'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__' 
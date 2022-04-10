# in this file I only create form for register for now
# the form for login was written manually in the html
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="nickname", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="confirm password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="email address", widget=forms.EmailInput(attrs={'class': 'form-control'}))


class ChangePwForm(forms.Form):
    oldpassword = forms.CharField(label="old password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    newpassword = forms.CharField(label="new password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

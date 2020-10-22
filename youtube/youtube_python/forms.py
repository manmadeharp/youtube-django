from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=50);
    password = forms.CharField(label='Your password', max_length=50);

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50);
    password = forms.CharField(label='Password', max_length=50);
    email = forms.CharField(label='Email', max_length=50);

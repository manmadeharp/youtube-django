from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50);
    password = forms.CharField(label='Password', max_length=50);

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50);
    password = forms.CharField(label='Password', max_length=50);
    email = forms.CharField(label='Email', max_length=50);

class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50);
    description = forms.CharField(label='Description', max_length=50);
    file = forms.FileField();



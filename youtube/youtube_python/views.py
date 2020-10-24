from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, NewVideoForm
from django.contrib.auth.models import User

class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'title'
        return render(request, self.template_name, {'menu_active_item': 'home'})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('already logged in. Redirecting')
            print(request.user)
            logout(request)
            return HttpResponseRedirect('/')
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('successful login')
                return HttpResponseRedirect('/')
            else:
                print('login failed')
                return HttpResponseRedirect('/login')
        return HttpResponse('this is login view this is POST request')


class RegisterView(View):
    template_name = 'register.html'
    def get(self, request):
        if request.user.is_authenticated:
            print('already logged in. Redirecting')
            print(request.user)
            return HttpResponseRedirect('/')
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            check_email=User.objects.get(email=email)
            if check_email is not None:
                return 'That email is already taken'
            user = User(username=username, email=email)
            user.set_password(password)
            print(user)
            user.save()
            print(user)
            return HttpResponseRedirect('/login')
        return HttpResponse('this is Register view this is POST request')


class NewVideo(View):
    template_name = 'newvideo.html'

    def get(self, request):
        variableA = 'new video'
        form = NewVideoForm()
        return render(request, self.template_name, {'variableA': variableA, 'form': form})

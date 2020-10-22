from django.views.generic.base import View, HttpResponse
from django.shortcuts import render
from .forms import LoginForm, RegisterForm

class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'title'
        return render(request, self.template_name, {'variableA': variableA})

class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        print('hello this is post')
        return HttpResponse('this is login view this is POST request')

class RegisterView(View):
    template_name = 'register.html'
    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        print('hello this is post')
        return HttpResponse('this is Register view this is POST request')

class NewVideo(View):
    template_name = 'newvideo.html'
    def get(self, request):
        variableA = 'new video'
        form = FormClass()
        return render(request, self.template_name, {'variableA': variableA, 'form': form})

from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

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
        print(request)
        return HttpResponse('this is login view this is POST request')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
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
        form = FormClass()
        return render(request, self.template_name, {'variableA': variableA, 'form': form})

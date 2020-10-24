from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, NewVideoForm
from django.contrib.auth.models import User
from .models import Video, Comment
import string, random


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        most_recent_videos = Video.objects.order_by('-datetime')[:10]
        return render(request, self.template_name, {'menu_active_item': 'home',
                                                    'most_recent_videos': most_recent_videos})


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
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/login')
        return HttpResponse('this is Register view this is POST request')


class NewVideo(View):
    template_name = 'newvideo.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/register')
        form = NewVideoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NewVideoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']

            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path = random_char + file.name

            newvideo = Video(title=title, description=description, user=request.user, path=path)
            newvideo.save()

            return HttpResponseRedirect('/video{}/'.format(newvideo.id))
        else:
            return HttpResponse('not valid go back and try again')


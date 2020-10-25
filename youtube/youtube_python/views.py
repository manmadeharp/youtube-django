from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, NewVideoForm, CommentForm
from django.contrib.auth.models import User
from .models import Video, Comment
import string, random
from django.core.files.storage import FileSystemStorage
import os
from wsgiref.util import FileWrapper


class VideoFileView(View):
    def get(self, request, file_name):
        BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
        file = FileWrapper(open(BASE_DIR + '/' + file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        most_recent_videos = Video.objects.order_by('-datetime')[:10]
        return render(request, self.template_name, {'menu_active_item': 'home',
                                                    'most_recent_videos': most_recent_videos})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class VideoView(View):
    template_name = 'video.html'

    def get(self, request, id):
        video_by_id = Video.objects.get(id=id)
        BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
        video_by_id.path = 'http://localhost:8000/get_video/' + video_by_id.path
        context = {'video': video_by_id}
        if request.user.is_authenticated:
            print('User Signed in')
            comment_form = CommentForm()
            context['form'] = comment_form
        comments = Comment.objects.filter(video_id=id).order_by('-datetime')[:5]
        print(comments)
        context['comments'] = comments
        return render(request, self.template_name, context)


class CommentView(View):
    template_name = 'comment.html'

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            videoid = request.POST['video']
            video = Video.objects.get(id=videoid)
            newcomment = Comment(text=text, user=request.user, video=video)
            newcomment.save()
            return HttpResponseRedirect('/video/{}'.format(str(videoid)))
        return HttpResponse('this is login view this is POST request')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
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
            fs = FileSystemStorage(location=os.path.dirname(os.path.dirname(os.path.abspath((__file__)))))
            filename = fs.save(path, file)
            file_url = fs.url(filename)
            print(fs)
            print(filename)
            print(file_url)
            newvideo = Video(title=title, description=description, user=request.user, path=path)
            newvideo.save()

            return HttpResponseRedirect('/video{}/'.format(newvideo.id))
        else:
            return HttpResponse('not valid go back and try again')

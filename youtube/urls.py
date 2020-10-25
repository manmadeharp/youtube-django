import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from .youtube_python.views import HomeView, NewVideo, LoginView, RegisterView, VideoView, CommentView, VideoFileView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('newvideo', NewVideo.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('video/<int:id>', VideoView.as_view()),
    path('comment', CommentView.as_view()),
    path('get_video/<file_name>', VideoFileView.as_view()),
    path('logout', LogoutView.as_view())
]

from django.conf import settings
from django.conf.urls import include, url
from django.urls import include,path

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns


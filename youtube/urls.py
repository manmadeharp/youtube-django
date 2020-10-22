import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from .youtube_python.views import HomeView, NewVideo, LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('newvideo', NewVideo.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view())
]

from django.conf import settings
from django.conf.urls import include, url
from django.urls import include,path

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns


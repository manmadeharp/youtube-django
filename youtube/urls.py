import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from .youtube_python.views import Index, NewVideo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', Index.as_view()),
    path('__debug__/', include(debug_toolbar.urls)),
    path('newvideo', NewVideo.as_view())

]

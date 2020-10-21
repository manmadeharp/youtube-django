from django.views.generic.base import View, HttpResponse
from django.shortcuts import render

class Index(View):
    template_name = 'index.html'
    def get(self, request):
        variableA = 'some text here'
        return render(request, self.template_name, {'variableA': variableA})

class NewVideo(View):
    template_name = 'newvideo.html'
    def get(self, request):
        variableA = 'some text here'
        return render(request, self.template_name, {'variableA': variableA})
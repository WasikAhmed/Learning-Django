from django.shortcuts import render

# importing loading form django template
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def index(request):
    template = loader.get_template('index.html')
    names = {
        'name':'Wasik'
    }
    return HttpResponse(template.render(names))

@require_http_methods(["GET"])
def welcome(request):
    template = loader.get_template('hello.html')
    names = {
        'myName': 'Wasik',
    }
    return HttpResponse(template.render(names))
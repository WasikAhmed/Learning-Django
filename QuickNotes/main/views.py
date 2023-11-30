from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(response):
    return render(response, "main/index.html", {})


def create(response):
    return render(response, "main/create.html", {})


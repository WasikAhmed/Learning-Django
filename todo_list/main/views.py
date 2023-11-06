from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import ToDoList, Item
from main.forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # item = ls.item_set.get(id=1)
    # return HttpResponse("<h1>%s</h1></br><p>%s</p>" %(ls.name, str(item.text)))
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {"na me":"test"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    
    return render(response, "main/create.html", {"form":form})
from django.contrib import admin
from main.models import ToDoList, Item

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
from django.db import models

# Create your models here.
class NoteList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Note(models.Model):
    notelist = models.ForeignKey(NoteList, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    userName = models.CharField(max_length=30)
    contents = models.TextField()
    lookup = models.IntegerField(default=0)

class Comment(models.Model):
    commentid = models.IntegerField(null =True)
    author = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=1000, null=True)
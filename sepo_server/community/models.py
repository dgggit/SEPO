from django.contrib.auth.models import User
from django.db import models

class Post_Community(models.Model):
    titie = models.CharField(max_length=1024)
    body = models.CharField(max_length=19200)
    author = models.ForeignKey(User)
    regdate = models.DateTimeField(auto_created = True, auto_now_add = True)
    hits= models.IntegerField(null=True, blank = True)

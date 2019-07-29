import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
STATUS = ((0,'Draft'),(1,'Publish'))
class Post(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=200,unique=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    description=models.CharField(max_length=500)
    content = models.CharField(max_length=1000)
    published_on=models.DateTimeField('published_on',auto_now_add=True)
    updated_on=models.DateTimeField('updated_on',auto_now=True)
    status=models.IntegerField(choices=STATUS, default=0)
    votes=models.IntegerField(default=0)
    class Meta:
        ordering=['-published_on']
    def is_published():
        if(published_on):
            return True
        else: 
            return False

    def __str__(self):
        return self.title
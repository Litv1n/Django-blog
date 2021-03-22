from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('Picture', default='', upload_to='posts/')

    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

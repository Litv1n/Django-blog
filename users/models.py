from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        'Avatar', default='avatar.jpeg', upload_to='avatars/')

    def __str__(self):
        return f'{self.user.username}'

    def save(self):
        super().save()

        image = Image.open(self.avatar.path)

        if image.height > 250 or image.width > 250:
            resize = (250, 250)
            image.thumbnail(resize)
            image.save(self.avatar.path)

from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import json


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    liked_comments = models.TextField(default='[]')
    liked_child_comments = models.TextField(default='[]')

    def __str__(self):
        return f'{self.user.username} Profile'

    def set_liked_comments(self, s):
        self.liked_comments = json.dumps(s)

    def get_liked_comments(self):
        return json.loads(self.liked_comments)

    def set_liked_child_comments(self, s):
        self.liked_child_comments = json.dumps(s)

    def get_liked_child_comments(self):
        return json.loads(self.liked_child_comments)


"""
    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
"""


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

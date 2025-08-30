from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True, default='')
    profileimg = CloudinaryField(
        'image',
        default='profile_images/default_profile'   # ✅ public_id, not URL
    )
    location = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = CloudinaryField('image')  # ✅ stored on Cloudinary
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return f"Post by {self.user} at {self.created_at}"
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Followers(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    writer = models.CharField(max_length=255)
    content = models.TextField()
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.title


class Image(models.Model):
    blog = models.ForeignKey(Post, related_name="pictures")
    image = models.ImageField(upload_to='blog_images', blank=True)
    caption = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u'%s' % self.blog

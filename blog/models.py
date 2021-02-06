from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify


User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(blank=True, upload_to='post_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    

class Comment(models.Model):
    content = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')



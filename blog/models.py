from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField()
    abstract = models.CharField(max_length=255, help_text="Tóm tắt cơ bản về bài viết")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_at = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def __unicode__(self):
       return '%s' % self.title
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
       return '%s' % self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
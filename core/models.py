from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.encoding import smart_text
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField


PUBLISH_CHOICES = [
    ('private', 'Private'),
    ('public', 'Public'),
]

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=300, default="Asif Ikbal")
    author_description = models.TextField(
        default="a short descrition of author")
    author_profile_picture = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    title = models.CharField(
        max_length=2000, verbose_name='Post Title', unique=True, error_messages={
            "unique": "Enter unique title."
        })
    post_content = HTMLField()
    overview = HTMLField()
    thumbnail = models.ImageField(upload_to='pics')
    date_of_publish = models.DateField(default=timezone.now)
    published = models.CharField(
        max_length=250, choices=PUBLISH_CHOICES, default=None)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    youtube = models.BooleanField(default=False)
    slug = models.SlugField(max_length=1000, blank=True, primary_key=True)
    public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title


class HomeBanner(models.Model):
    banner_image = models.ImageField(upload_to='pics')
    banner_Heading = models.CharField(max_length=1000)
    banner_description = models.TextField()
    date = models.DateField(default=timezone.now)
    featured = models.BooleanField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.banner_Heading


class Queries(models.Model):
    author_name = models.CharField(max_length=250)
    author_email = models.EmailField()
    message = models.TextField()
    solved_status = models.BooleanField(default=True)

    def __str__(self):
        return self.author_name

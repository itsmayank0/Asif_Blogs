from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.encoding import smart_text
from django.contrib.auth import get_user_model


PUBLISH_CHOICES = [
    ('private', 'Private'),
    ('public', 'Public'),
]

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    title = models.CharField(
        max_length=2000, verbose_name='Post Title', unique=True, error_messages={
            "unique": "Enter unique title."
        })
    post_description = models.TextField(blank=True, null=True)
    overview = models.TextField(default="Default short des.")
    thumbnail = models.ImageField(upload_to='pics', blank=True)
    date_of_publish = models.DateField(auto_now_add=True)
    published = models.CharField(
        max_length=250, choices=PUBLISH_CHOICES, default=None)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    youtube = models.BooleanField(default=False)
    slug = models.SlugField(max_length=1000, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'


class HomeBanner(models.Model):
    banner_image = models.ImageField(upload_to='pics')
    banner_Heading = models.CharField(max_length=1000)
    banner_description = models.TextField()
    date = models.DateField(default=timezone.now)
    featured = models.BooleanField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.banner_Heading

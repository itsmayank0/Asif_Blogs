from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.encoding import smart_text


PUBLISH_CHOICES = [
    ('private', 'Private'),
    ('public', 'Public'),
]


class BlogPost(models.Model):
    title = models.CharField(
        max_length=2000, verbose_name='Post Title', unique=True, error_messages={
            "unique": "Enter unique title."
        })
    post_description = models.TextField(blank=True, null=True)
    post_short_description = models.TextField(default="Default short des.")
    post_images = models.ImageField(upload_to='pics', blank=True)
    date_of_publish = models.DateField(default=timezone.now)
    published = models.CharField(
        max_length=250, choices=PUBLISH_CHOICES, default=None)
    author_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=1000, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'


class EmailList(models.Model):
    user_name = models.CharField(max_length=300)
    user_email = models.EmailField()

    class Meta:
        verbose_name = 'Users Email List'
        verbose_name_plural = 'Users Email List'

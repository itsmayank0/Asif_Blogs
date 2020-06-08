# Generated by Django 3.0.7 on 2020-06-08 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'unique': 'Enter unique title.'}, max_length=2000, unique=True, verbose_name='Post Title')),
                ('post_description', models.TextField(blank=True, null=True)),
                ('post_images', models.ImageField(upload_to='pics')),
                ('date_of_publish', models.DateField(default=django.utils.timezone.now)),
                ('published', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default=None, max_length=250)),
                ('author_name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
    ]

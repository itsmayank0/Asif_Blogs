# Generated by Django 3.0.7 on 2020-06-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200614_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='profile_picture',
            new_name='author_profile_picture',
        ),
        migrations.AddField(
            model_name='author',
            name='author_description',
            field=models.TextField(default='a short descrition of author'),
        ),
        migrations.AddField(
            model_name='author',
            name='author_name',
            field=models.CharField(default='Asif Ikbal', max_length=300),
        ),
    ]
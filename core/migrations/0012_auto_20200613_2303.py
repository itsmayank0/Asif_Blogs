# Generated by Django 3.0.7 on 2020-06-13 17:33

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200613_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='post_description',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_content',
            field=tinymce.models.HTMLField(default='this is demo content'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-12 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_emaillist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='post_images',
            new_name='thumbnail',
        ),
    ]

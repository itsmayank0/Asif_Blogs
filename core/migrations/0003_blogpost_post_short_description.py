# Generated by Django 3.0.7 on 2020-06-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200608_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_short_description',
            field=models.TextField(default='Default short des.'),
        ),
    ]

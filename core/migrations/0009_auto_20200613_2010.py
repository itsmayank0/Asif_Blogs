# Generated by Django 3.0.7 on 2020-06-13 14:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_blogpost_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_of_publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

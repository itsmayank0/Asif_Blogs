from django.db import models

# Create your models here.


class EmailList(models.Model):
    user_name = models.CharField(max_length=300)
    user_email = models.EmailField()

    class Meta:
        verbose_name = 'Users Email List'
        verbose_name_plural = 'Users Email List'

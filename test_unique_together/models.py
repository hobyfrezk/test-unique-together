from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=255)
    dummy_column = models.CharField(max_length=255)

    class Meta:
        unique_together = (
            ('user', 'dummy_column'),
        )
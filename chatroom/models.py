from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

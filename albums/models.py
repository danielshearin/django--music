from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    created_at = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.title
    
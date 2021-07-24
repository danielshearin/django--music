from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

    
class Artist(models.Model):
    artist = models.CharField(max_length=40)

    def __str__(self):
        return self.artist
    
    class Meta:
        ordering = ['artist']

class Album(models.Model):
    title = models.CharField(max_length=40)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    favorite = models.BooleanField(blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

    
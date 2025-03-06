from django.db import models
from django.urls import reverse

class Song(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    date = models.DateField()
    length = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('song-detail', kwargs={'song_id': self.id})
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
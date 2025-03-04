from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    date = models.DateField('Date Published')
    length = models.IntegerField('Length of Song')

    def __str__(self):
        return self.name

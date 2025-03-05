from django.shortcuts import render
from .models import Song

def home(request):    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def song_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', {'songs': songs})

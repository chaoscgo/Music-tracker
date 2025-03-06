from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Song

def home(request):    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def song_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', {'songs': songs})

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'songs/detail.html', {'song': song})

class SongCreate(CreateView):
    model = Song
    fields = ['name', 'genre', 'artist', 'date', 'length']

class SongUpdate(UpdateView):
    model = Song
    fields = ['name', 'genre', 'artist', 'date', 'length']

class SongDelete(DeleteView):
    model = Song
    success_url = '/songs/'



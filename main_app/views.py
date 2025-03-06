from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Song
from .forms import ArtistForm

def home(request):    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def song_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', {'songs': songs})

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    artist_form = ArtistForm()
    return render(request, 'songs/detail.html', {'song': song, 'artist_form': artist_form})

def add_artist(request, song_id):
    form = ArtistForm(request.POST)
    if form.is_valid():
        new_artist = form.save(commit=False)
        new_artist.song_id = song_id
        new_artist.save()
    return redirect('song-detail', song_id=song_id)

class SongCreate(CreateView):
    model = Song
    fields = ['name', 'genre', 'artist', 'date', 'length']

class SongUpdate(UpdateView):
    model = Song
    fields = ['name', 'genre', 'artist', 'date', 'length']

class SongDelete(DeleteView):
    model = Song
    success_url = '/songs/'



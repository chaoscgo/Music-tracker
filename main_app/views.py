from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Song
from .forms import ArtistForm
from django.contrib.auth.views import LoginView

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('song-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def home(request):    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def song_index(request):
    songs = Song.objects.filter(user=request.user)
    return render(request, 'songs/index.html', {'songs': songs})

@login_required
def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    artist_form = ArtistForm()
    return render(request, 'songs/detail.html', {'song': song, 'artist_form': artist_form})

@login_required
def add_artist(request, song_id):
    form = ArtistForm(request.POST)
    if form.is_valid():
        new_artist = form.save(commit=False)
        new_artist.song_id = song_id
        new_artist.save()
    return redirect('song-detail', song_id=song_id)

class Home(LoginView):
    template_name = 'home.html'

class SongCreate(LoginRequiredMixin, CreateView):
    model = Song
    fields = ['name', 'genre', 'date', 'length']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SongUpdate(LoginRequiredMixin, UpdateView):
    model = Song
    fields = ['name', 'genre', 'date', 'length']

class SongDelete(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = '/songs/'



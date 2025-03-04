from django.shortcuts import render

class Song:
    def __init__(self, name, artist, genre, date, length):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.date = date
        self.length = length

songs = [
    Song("Dragula", 'Rob Zombie', 'Hard Rock', '8/24/1998', 4),
    Song("She's Been Through the Fire", 'Brian Rhea', 'Country', '6/10/2022', 4),
    Song("Love the Hell Out of You", 'Lewis Capaldi', 'Alternative', '5/19/2023', 3),
    Song("Used to Be Young", 'Miley Cyrus', 'Pop', '8/25/2023', 3),
]


def home(request):    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def song_index(request):
    return render(request, 'songs/index.html', {'songs': songs})

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.song_index, name='song-index'),
    path('songs/<int:song_id>/', views.song_detail, name='song-detail'),
    path('songs/create/', views.SongCreate.as_view(), name='song-create'),
    path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='song-update'),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='song-delete'),
    path('songs/<int:song_id>/add-artist/', views.add_artist, name='add-artist'),
]


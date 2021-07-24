from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('title', views.album_list_title, name='album_list_title'),
    path('year', views.album_list_year, name='album_list_year'),
    path('favorite', views.album_list_favorite, name='album_list_favorite'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    # path('album/new/', views.album_new, name='album_new'),
    path('album/new/', views.create_artist, name='album_new'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
    path('artist/<int:pk>', views.artist_page, name='artist_page'),
    path('album/<int:pk>/favorite/', views.album_favorite, name='album_favorite'),
    path('album/<int:pk>/not_favorite/', views.album_not_favorite, name='album_not_favorite'),
]
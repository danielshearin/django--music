from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Album, Artist
from .forms import AlbumForm, AlbumFormSet
from .forms import ArtistForm, AlbumArtistForm, OrderByForm
from django.utils.datastructures import MultiValueDictKeyError



def album_list(request):
    albums = Album.objects.order_by('artist', 'title')
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_list_title(request):
    albums = Album.objects.order_by('title')
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_list_year(request):
    albums = Album.objects.order_by('year', 'artist', 'title')
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_list_favorite(request):
    albums = Album.objects.order_by('-favorite', 'artist', 'title')
    return render(request, 'albums/album_list.html', {'albums': albums})




def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})


# def create_artist(request):
#     if request.method == "GET":
#         form = ArtistForm()
#         formset = AlbumFormSet()
#         return render(request, 'albums/create_artist.html', {'form':form, 'formset':formset})
#     elif request.method == "POST":
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             artist = form.save()
#             formset = AlbumFormSet(request.POST, instance=artist)
#             # album = form.save(commit=False)
#             album = form.save()
#             if formset.is_valid():
#                 formset.save()
#             # album.author = request.user
#             # album.save()
#             return redirect('album_detail', pk=album.pk)
        
    

def album_new(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        # artist_form = ArtistForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm
    return render(request, 'albums/album_edit.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html', {'form': form})
    
def album_delete(request, pk):
    album_to_delete = get_object_or_404(Album, pk=pk)
    album_to_delete.delete()
    return redirect('album_list')

def album_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.favorite = True
    album.save()
    return redirect('album_detail', pk=album.pk)

def album_not_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.favorite = False
    album.save()
    return redirect('album_detail', pk=album.pk)

def artist_page(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'albums/artist_page.html', {'artist': artist})

def create_artist(request):
    if request.method == "GET":
        form = AlbumArtistForm()
        return render(request, 'albums/create_artist.html', {'form':form})
    elif request.method == "POST":
        form = AlbumArtistForm(request.POST)
        # breakpoint()
        if form.is_valid():
            title = form.data['title']
            artist = form.data['artist']
            year = form.data['year']
            try:
                favorite = form.data['favorite']
                if favorite == 'on':
                    favorite = True
                # else:
                #     favorite = False
            except MultiValueDictKeyError:
                favorite = False
            validated_artist = Artist.objects.get_or_create(artist=artist)[0]
            album = Album.objects.create(artist=validated_artist, title=title, year=year, favorite=favorite)
            album.save()
            return redirect('album_detail', pk=album.pk)
        
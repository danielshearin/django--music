from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Album
from .forms import AlbumForm


def album_list(request):
    # albums = Album.objects.filter(created_at__lte=timezone.now().order_by('published_date'))
    albums = Album.objects.order_by('created_at')
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})

def album_new(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
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
    

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Album


def album_list(request):
    # albums = Album.objects.filter(created_at__lte=timezone.now().order_by('published_date'))
    albums = Album.objects.order_by('created_at')
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})
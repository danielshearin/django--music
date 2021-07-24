from django import forms
from django.db.models.fields import CharField
from django.forms.models import inlineformset_factory
from .models import Album
from .models import Artist
        

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('artist',)

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'year', 'favorite',)
        
AlbumFormSet = forms.inlineformset_factory(Artist, Album, form =AlbumForm, extra=1)
        
        
class AlbumArtistForm(forms.Form):
    title = forms.CharField(max_length=40)
    artist = forms.CharField(max_length=40)
    year = forms.IntegerField()
    favorite = forms.BooleanField(required=False)
    
class OrderByForm(forms.Form):
    order = CharField(max_length=20)
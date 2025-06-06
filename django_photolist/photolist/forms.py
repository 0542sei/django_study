from django import forms
from .models import Photo  #== from photolist import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields={
            "title",
            "author",
            "image",
            "description",
            "price"
        }


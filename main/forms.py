from .models import Film
from django.forms import ModelForm, TextInput


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'description', 'genre', 'author']
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "id": "name",
                "aria-describedby": "nameHelp",
                "placeholder": "название фильма к просмотру",
                "type": "text"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "id": "description",
                "aria-describedby": "descriptionHelp",
                "placeholder": "описание фильма",
                "type": "text"
            }),
            "genre": TextInput(attrs={
                "class": "form-control",
                "id": "genre",
                "aria-describedby": "genreHelp",
                "placeholder": "жанр фильма (можно несколько)",
                "type": "text"
            }),
            "author": TextInput(attrs={
                "class": "form-control",
                "id": "author",
                "aria-describedby": "authorHelp",
                "placeholder": "режисер фильма",
                "type": "text"
            }),
        }

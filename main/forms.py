from .models import Film
from django.forms import ModelForm, TextInput


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['id', 'name', 'description', 'genre', 'author']
        widgets = {
            "id": TextInput(attrs={
                "class": "form-control",
                "id": "id",
                "type": "text"
            }),
            "name": TextInput(attrs={
                "class": "form-control",
                "id": "name",
                "aria-describedby": "nameHelp",
                "placeholder": "введите название фильма для добавления в базу",
                "type": "text"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "id": "description",
                "aria-describedby": "descriptionHelp",
                "placeholder": "введите краткое описание фильма (не обязательно)",
                "type": "text"
            }),
            "genre": TextInput(attrs={
                "class": "form-control",
                "id": "genre",
                "aria-describedby": "genreHelp",
                "placeholder": "введите жанр фильма (можно несколько)",
                "type": "text"
            }),
            "author": TextInput(attrs={
                "class": "form-control",
                "id": "author",
                "aria-describedby": "authorHelp",
                "placeholder": "введите режисера фильма",
                "type": "text"
            }),
        }

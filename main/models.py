from django.db import models


# Create your models here.
class Film(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100) # название фильма
    score = models.FloatField(verbose_name='Score', blank=True) # оценка фильма после просмотра
    description = models.TextField(verbose_name='Description', max_length=256, blank=True) # описание фильма
    genre = models.TextField(verbose_name='Genre', max_length=100, blank=False) # жанр фильма
    author = models.TextField(verbose_name='Author', max_length=100, blank=False) # автор фильма (режисер)
    comment = models.TextField(verbose_name='Comment', max_length=100, blank=True) # комментарий к фильму
    viewed = models.DateTimeField(verbose_name='Viewed', blank=True) # дата просмотра фильма

    def __str__(self):
        return f"{self.name} - {self.author} - {self.genre}"

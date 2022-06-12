from django.db import models


# Create your models here.
class Film(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, blank=False, null=False) # название фильма
    score = models.FloatField(verbose_name='Score', blank=True, null=True) # оценка фильма после просмотра
    description = models.TextField(verbose_name='Description', max_length=256, blank=True, null=True) # описание фильма
    genre = models.TextField(verbose_name='Genre', max_length=100, blank=False, null=False) # жанр фильма
    author = models.TextField(verbose_name='Author', max_length=100, blank=False, null=False) # автор фильма (режисер)
    comment = models.TextField(verbose_name='Comment', max_length=100, blank=True, null=True) # комментарий к фильму
    viewed = models.DateField(verbose_name='Viewed', blank=True, null=True) # дата просмотра фильма
    isDeleted = models.BooleanField(verbose_name='isDeleted', blank=True, null=True) # удален ли фильм из БД
    deleted = models.DateField(verbose_name='Deleted', blank=True, null=True) # дата удаления фильма из БД

    def __str__(self):
        return f"{self.name} - {self.author} - {self.genre}"



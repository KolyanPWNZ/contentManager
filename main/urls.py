from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('Фильмы к просмотру', views.movies_to_watch, name='movies_to_watch'),
]
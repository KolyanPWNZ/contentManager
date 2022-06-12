from django.shortcuts import render
from django.core.paginator import Paginator
import datetime

from .models import Film
from .forms import FilmForm


# Create your views here.
def index(request):
    films = Film.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {
                      "title": "Main page",
                      "header": "to-do list",
                      "films": films,
                  })



def movies_viewed(request):
    if request.method == 'POST':
        if 'add_film_in_db' in request.POST:
            form = FilmForm(request.POST)
            if form.is_valid():
                form.save()

    form = FilmForm()
    films = Film.objects.order_by('-id')
    films = [film for film in films if film.viewed and not film.deleted]

    paginator = Paginator(films, 5)
    page_number = request.GET.get('page', 1)
    films_page = paginator.get_page(page_number)

    context = {
        'form': form,
        "films": films_page,
        "page_number": page_number
    }
    return render(request, 'main/movies_viewed.html', context)


def movies_to_watch(request):
    if request.method == 'POST':
        if 'add_film_in_db' in request.POST:
            form = FilmForm(request.POST)
            if form.is_valid():
                form.save()
        if 'selecter_action' in request.POST and 'selected_films' in request.POST:
            if request.POST['action'] == 'delete_selected':  # удаление фильмов из БД
                for filt_id in request.POST.getlist('selected_films'):
                    film = Film.objects.get(id=filt_id)
                    film.deleted = datetime.date.today()
                    film.isDeleted = True
                    film.save()
                    # ДОБАВИТЬ ЛОГИРОВАНИЕ

            if request.POST['action'] == 'viewed_selected':
                for filt_id in request.POST.getlist('selected_films'):
                    film = Film.objects.get(id=filt_id)
                    film.viewed = datetime.date.today()
                    film.save()
                    # ДОБАВИТЬ ЛОГИРОВАНИЕ

    form = FilmForm()
    films = Film.objects.order_by('-id')
    films = [film for film in films if not film.viewed and not film.isDeleted]

    paginator = Paginator(films, 5)
    page_number = request.GET.get('page', 1)
    films_page = paginator.get_page(page_number)


    context = {
        'form': form,
        "films": films_page,
        "page_number": page_number
    }
    return render(request, 'main/movies_to_watch.html', context)

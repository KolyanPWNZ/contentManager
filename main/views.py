from django.shortcuts import render
from django.core.paginator import Paginator

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



def movies_to_watch(request):
    form = FilmForm()
    films = Film.objects.order_by('-id')
    paginator = Paginator(films, 2)

    page_number = request.GET.get('page', 1)
    films_page = paginator.get_page(page_number)

    if request.method == 'POST':
        if 'add_film_in_db' in request.POST:
            form = FilmForm(request.POST)
            if form.is_valid():
                form.save()
        if 'selecter_action' in request.POST and 'selected_films' in request.POST:
            print("YES")
            print(request.POST)
            if request.POST['action'] == 'delete_selected':
                for fild_id in request.POST.getlist('selected_films'):
                    Film.objects.filter(id=fild_id).delete()

    context = {
        'form': form,
        "title": "Publication",
        "header": "My publication",
        "films": films_page,
        "page_number": page_number
    }
    return render(request, 'main/movies_to_watch.html', context)

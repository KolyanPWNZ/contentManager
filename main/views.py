from django.shortcuts import render

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
    context = {
        'form': form,
        "title": "Publication",
        "header": "My publication",
        "posts": films,
    }
    return render(request, 'main/movies_to_watch.html', context)


# def task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     form = TaskForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'main/task.html', context)
#
#
# def post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     if request.method == 'GET':
#         form = PostForm(request.GET)
#         if form.is_valid():
#             print(form)
#
#     form = PostForm()
#     posts = Post.objects.order_by('-id')
#     context = {
#         'form': form,
#         "title": "Publication",
#         "header": "My publication",
#         "posts": posts,
#     }
#     return render(request, 'main/post.html', context)
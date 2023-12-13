from django.shortcuts import render

# import models.y (database) we can remove the dummy data from here
from .models import Post
# Create your views here.


def home(request):
    context = {"posts": Post.objects.all()}  # add the Post.objects.all() from databases
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})

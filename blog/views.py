from django.shortcuts import render
from .models import BlogPost


def index(request):
    slug = "Scorption"
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/index.html", context={"blog_post" : post})

from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required

from blog.models import BlogPost
from django.shortcuts import redirect



def index(request):
    r = HttpResponse()
    r.content = "{'1' : 'mojombo'}"
    r.status_code = 404
    r['content_type'] = 'application/json'
    return redirect("home")


@login_required
def test(request):
    return JsonResponse({"1": "Mark zukerberg"})
"""


"""

def blog (request):

    try :
        blog_post = BlogPost.objects.get(pk=1)
    except BlogPost.DoesNotExist:
        raise  Http404("L'article n'existe pas dans la base de donnée")
    return HttpResponse(blog_post.content)

def home(request):
    return HttpResponse("salut")



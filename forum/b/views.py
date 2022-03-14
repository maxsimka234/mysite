from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    post_list=models.Post.objects.all()
    return render(request,"b/index.html" ,{
        "post_list":post_list,
    })

def post_page_view(request , post_id):
    return HttpResponse("this is a post num: "+str(post_id))    
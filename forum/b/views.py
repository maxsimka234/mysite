from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    post_list=models.Post.objects.all()
    return render(request,"b/index.html" ,{
        "post_list":post_list,
    })

def post_page_view(request , self_post_id):
    post=models.Post.objects.get(id=self_post_id)
    comments_list=models.Comment.objects.filter(post_id=self_post_id)
    return render(request,'b/post.html',{
        'post' :post,
        'comments_list' : comments_list,
    })    
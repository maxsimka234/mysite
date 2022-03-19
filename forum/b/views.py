from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
import datetime
from requests import post
from . import models
from .import forms

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

def add_coment(request, self_post_id):
    form=forms.AddCommentForm(request.POST)
    if form.is_valid():
        models.Comment.objects.create(post_id=models.Post.objects.get(id=self_post_id) , comment_author=form.cleaned_data["comment_author"],
         comment_text=form.cleaned_data["comment_text"] , comment_pub_date=datetime.datetime.now() )
        return HttpResponseRedirect(reverse("post_page",args=str(self_post_id)))
    else:  
        return HttpResponse(request)    
        
def create_post(request):
    form=forms.CreatePostForm(request.POST)
    if form.is_valid():
        models.Post.objects.create(post_title=form.cleaned_data["post_titel"] ,post_text=form.cleaned_data["post_text"],
        post_pub_date=datetime.datetime.now() )    
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponse(request)    
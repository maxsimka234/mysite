
from http.client import NO_CONTENT
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
import datetime
from requests import post
import requests
from . import models
from .import forms
import json
import urllib

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
            ''' Begin reCAPTCHA validation '''
        
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                models.Comment.objects.create(post_id=models.Post.objects.get(id=self_post_id) , comment_author=form.cleaned_data["comment_author"],
                                                 comment_text=form.cleaned_data["comment_text"] , comment_pub_date=datetime.datetime.now() )
                return HttpResponseRedirect(reverse("post_page",args=str(self_post_id)))
            else:
                return HttpResponseRedirect(reverse("post_page",args=str(self_post_id)))       
    else: 
        return HttpResponse(request)    
        
def create_post(request):
    form=forms.CreatePostForm(request.POST)
    if form.is_valid():
            ''' Begin reCAPTCHA validation '''
        
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''
            
            if result['success']:
                models.Post.objects.create(post_title=form.cleaned_data["post_titel"] ,post_text=form.cleaned_data["post_text"],
                post_pub_date=datetime.datetime.now() )    
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('index'))   
    else:
        return HttpResponse(request)    
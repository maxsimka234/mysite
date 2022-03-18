
from unicodedata import name
from django.urls import path , include 
from . import views

urlpatterns = [
    path('' ,views.index ,name="index"),
    path("<int:self_post_id>/",views.post_page_view, name="post_page"),
    path("<int:self_post_id>/add_comment/" , views.add_coment ,name="add_comment"),
]


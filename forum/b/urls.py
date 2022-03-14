
from django.urls import path , include 
from . import views

urlpatterns = [
    path('' ,views.index ,name="index"),
    path("<int:self_post_id>/",views.post_page_view, name="post_page")
]


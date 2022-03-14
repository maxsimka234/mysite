from tkinter import CASCADE
from django.db import models

class Post(models.Model):
    post_title=models.CharField(max_length=100)
    post_text=models.CharField(max_length=500)
    post_pub_date=models.DateTimeField()

    def __str__(self) :
        return(self.post_title)


class Comment(models.Model):
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_author=models.CharField(max_length=50)
    comment_text=models.CharField(max_length=200)
    comment_pub_date=models.DateTimeField()

    def __str__(self):
        return(self.comment_author+" "+str(self.comment_pub_date))
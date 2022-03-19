from django import forms

class CreatePostForm(forms.Form):
    post_titel=forms.CharField(max_length=100)
    post_text=forms.CharField(max_length=500)

class AddCommentForm(forms.Form):
    comment_author=forms.CharField(max_length=50)
    comment_text=forms.CharField(max_length=200)
from django import forms

class AddCommentForm(forms.Form):
    comment_author=forms.CharField(max_length=50)
    comment_text=forms.CharField(max_length=200)
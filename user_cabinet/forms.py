from django import forms

from blog.models import Client
from blog.models import Comment

class CabForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('user_photo',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'text',)
        exclude = ('data', 'post', 'author')
from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        exclude = ['Post']
        labels = {
            'author_name': 'Your Name',
            'text': 'Your Comment',
        }
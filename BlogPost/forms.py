from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    """
    Handles validation and rendering of user comments.
    The 'Post' field is intentionally excluded so users cannot attach their 
    comments to a different post by manipulating the form data.
    """
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        exclude = ['Post']
        labels = {
            'author_name': 'Your Name',
            'text': 'Your Comment',
        }
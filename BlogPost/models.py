from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    """
    Represents a blog author. 
    Separated from the standard User model to allow for external guest authors 
    without requiring them to have full system accounts.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    """
    The core blog post model.
    Uses a slug for SEO-friendly URLs and requires a minimum content length
    to ensure quality posts are published.
    """
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pictures", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    """
    User-submitted comments attached to specific posts.
    Deleted automatically if the parent post is removed (CASCADE).
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
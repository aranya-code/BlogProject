from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    """Renders the landing page with the main feed."""
    posts = Post.objects.all()
    return render(request, 'BlogPost/home.html', {'posts': posts})

def post_list(request):
    """Renders the dedicated index of all historical posts."""
    posts = Post.objects.all()
    return render(request, 'BlogPost/all-posts.html', {'posts': posts})


class SinglePostView(View):
    """
    Handles displaying a single post (GET) and submitting new comments (POST).
    Also checks if the user has saved this post to their session for later reading.
    """
    def is_stored_post(self, request, post_id):
        # Checks the user's browser session to see if they've bookmarked this post
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved_for_later = post_id in stored_posts
        else:
          is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"), # Ordering ensures newest comments appear first
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "BlogPost/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            # commit=False allows us to attach the parent post ID before hitting the database
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            # Redirecting via URL name prevents form resubmission if the user refreshes the page
            return HttpResponseRedirect(reverse("blog:post_detail", args=[slug]))

        context = {
            "post": post,
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "BlogPost/post-detail.html", context)


class ReadLaterView(View):
    """
    Manages the user's "Read Later" list using Django sessions.
    This architecture allows bookmarking without forcing the user to create an account.
    """
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          # Fetching all bookmarked posts in a single efficient query using the __in lookup
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "BlogPost/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        # Toggle functionality: add the post if not present, remove it if it was already saved
        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")
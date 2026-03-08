from django.test import TestCase, Client
from django.urls import reverse
from .models import Author, Post, Comment
from .forms import CommentForm

class TestModels(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Jane", 
            last_name="Doe", 
            email_address="jane@example.com"
        )
        self.post = Post.objects.create(
            title="My First Post",
            excerpt="This is a test excerpt.",
            slug="my-first-post",
            content="This content is definitely longer than 10 characters.",
            author=self.author
        )

    def test_author_full_name(self):
        self.assertEqual(self.author.full_name(), "Jane Doe")
        self.assertEqual(str(self.author), "Jane Doe")

    def test_post_string_representation(self):
        self.assertEqual(str(self.post), "My First Post")

    def test_comment_string_representation(self):
        comment = Comment.objects.create(
            post=self.post,
            author_name="John Smith",
            text="Great post!"
        )
        self.assertEqual(str(comment), "My First Post")


class TestForms(TestCase):
    def test_comment_form_valid(self):
        form = CommentForm(data={
            'author_name': 'Alice',
            'text': 'This is a fantastic read.'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_empty(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2) # Missing author_name and text


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(first_name="Jane", last_name="Doe", email_address="jane@example.com")
        self.post = Post.objects.create(
            title="Test Post",
            excerpt="Excerpt",
            slug="test-post",
            content="Content longer than 10 chars",
            author=self.author
        )

    def test_home_view(self):
        # Note: If you registered your app namespace, you might need reverse('blog:home')
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogPost/home.html')
        self.assertIn('posts', response.context)

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogPost/all-posts.html')

    def test_single_post_view_get(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogPost/post-detail.html')
        self.assertEqual(response.context['post'], self.post)
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_single_post_view_post_valid_comment(self):
        response = self.client.post(reverse('blog:post_detail', args=[self.post.slug]), {
            'author_name': 'Test User',
            'text': 'Test comment text.'
        })
        # Should redirect back to the same page after successful post
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.comments.count(), 1)
        self.assertEqual(self.post.comments.first().author_name, 'Test User')

    def test_read_later_view_add_to_session(self):
        # Test posting a post_id to the read later view
        response = self.client.post(reverse('blog:read_later'), {
            'post_id': self.post.id
        })
        self.assertEqual(response.status_code, 302) # Redirects to "/"
        self.assertEqual(self.client.session.get('stored_posts'), [self.post.id])

    def test_read_later_view_remove_from_session(self):
        # Setup the session with the post already in it
        session = self.client.session
        session['stored_posts'] = [self.post.id]
        session.save()

        # Post again to toggle (remove) it
        response = self.client.post(reverse('blog:read_later'), {
            'post_id': self.post.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get('stored_posts'), [])
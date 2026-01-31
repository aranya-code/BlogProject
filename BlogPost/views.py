from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

posts =[
{
        "slug": "hike-in-the-mountains",
        "image": "BlogPost/mountain.jpg",
        "author": "Nobody",
        "date": date(2026, 1, 31),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            The trail rises quietly as pine-scented air fills my lungs.
            Boots crunch over stone, each step a small promise upward.
            Clouds drift below like thoughts left behind in the valley.
            The wind tells old stories at the ridge’s sharp edge.
            At the summit, silence feels earned—and endlessly wide.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "BlogPost/coding.jpg",
        "author": "Anonymous",
        "date": date(2026, 1, 31),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Django templates provide a powerful way to separate the presentation layer from the business logic...
        """
    },
    {
        "slug": "into-the-woods",
        "image": "BlogPost/forest.jpg",
        "author": "NatureLover",
        "date": date(2026, 1, 31),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Forests are vital ecosystems that cover about 31% of the Earth's land area...
        """
    }
]

# Create your views here.
def home(request):
    return render(request, 'BlogPost/home.html', {'posts': posts})

def post_list(request):
    return render(request, 'BlogPost/all-posts.html', {'posts': posts})

def post_detail(request, slug):
    main_post = next((post for post in posts if post["slug"] == slug), None)
    return render(request, 'BlogPost/post-detail.html', {'post': main_post})
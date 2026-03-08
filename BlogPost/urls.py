from django.urls import path
from . import views

# Setting the app namespace prevents URL collisions if other apps also have a 'home' or 'post_list' route
app_name = 'blog'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('posts/', views.post_list, name = 'post_list'),
    path('posts/<slug:slug>/', views.SinglePostView.as_view(), name = 'post_detail'),
    path('read-later/', views.ReadLaterView.as_view(), name = 'read_later'),
]
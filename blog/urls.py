from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from blog.api.views import api_detail_post_view, api_update_post_view, api_delete_post_view, api_add_post_view

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    path('<title>/detail/', api_detail_post_view, name='api-post-detail'),
    path('<title>/update/', api_update_post_view, name='api-post-update'),
    path('<title>/delete/', api_delete_post_view, name='api-post-delete'),
    path('create/', api_add_post_view, name='api-post-create'),
]

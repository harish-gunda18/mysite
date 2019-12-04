from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, UserMyPostListView
from . import views
from blog.api.views import api_detail_post_view, api_update_post_view, api_delete_post_view, api_create_post_view, ApiPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),

    # non-api views
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/myposts/', UserMyPostListView.as_view(), name='user-my-posts'),
    path('about/', views.about, name='blog-about'),
    # api views
    path('<title>/details/', api_detail_post_view, name='api-post-detail'),
    path('<title>/update/', api_update_post_view, name='api-post-update'),
    path('<title>/delete/', api_delete_post_view, name='api-post-delete'),
    path('create/', api_create_post_view, name='api-post-create'),
    path('list/', ApiPostListView.as_view(), name='api-post-list'),
]

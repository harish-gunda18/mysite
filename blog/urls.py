from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView,\
    PostSearchListView, LatestPosts
from . import views
from blog.api.views import api_detail_post_view, api_update_post_view, api_delete_post_view, api_create_post_view,\
    ApiPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('search/', PostSearchListView.as_view(), name='blog-search'),
    # non-api views
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment-update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
    path('notification/<int:pk>/delete/', views.delete_notification, name='notification-delete'),
    path('childcomment/<int:pk>/update/', views.child_comment_update, name='child-comment-update'),
    path('childcomment/<int:pk>/delete/', views.child_comment_delete, name='child-comment-delete'),
    path('childcomment/<int:ppk>/<int:cpk>/create/', views.child_comment_create, name='child-comment-create'),
    path('about/', views.about, name='blog-about'),
    path('postlikeupdate/', views.update_post_likes, name='post-like-update'),
    path('commentlikeupdate/', views.update_comment_likes, name='comment-like-update'),
    path('childcommentlikeupdate/', views.update_child_comment_likes, name='child-comment-like-update'),
    path('latestposts/', LatestPosts.as_view(), name='latest-posts'),
    # api views
    path('<int:pk>/details/', api_detail_post_view, name='api-post-detail'),
    path('<title>/update/', api_update_post_view, name='api-post-update'),
    path('<title>/delete/', api_delete_post_view, name='api-post-delete'),
    path('create/', api_create_post_view, name='api-post-create'),
    path('list/', ApiPostListView.as_view(), name='api-post-list'),
]

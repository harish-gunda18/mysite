from rest_framework import serializers
from blog.models import Post, Comment, ChildComment
from django.contrib.auth.models import User


class ChildCommentViewSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = ChildComment
        fields = ['comment_text', 'date_posted', 'likes', 'author_username']


class CommentViewSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    child_comments = ChildCommentViewSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['comment_text', 'date_posted', 'likes', 'author_username', 'child_comments']


class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentViewSerializer(many=True, read_only=True)
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted', 'comments', 'author_username']

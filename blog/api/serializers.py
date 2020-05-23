from rest_framework import serializers
from blog.models import Post, Comment, ChildComment, Notification
from django.shortcuts import reverse


class ChildCommentViewSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    author_image = serializers.ImageField(source='author.profile.image')
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = ChildComment
        fields = ['comment_text', 'date_posted', 'likes', 'author_username', 'author_image', 'is_liked']

    def get_is_liked(self, obj):
        if obj.pk in self.context.get('user').childcommentlikes_set.all().values_list('child_comment__pk', flat=True):
            return True
        else:
            return False


class CommentViewSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    child_comments = ChildCommentViewSerializer(many=True, read_only=True)
    author_image = serializers.ImageField(source='author.profile.image')
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['comment_text', 'date_posted', 'likes', 'author_username', 'child_comments', 'author_image',
                  'is_liked']

    def get_is_liked(self, obj):
        if obj.pk in self.context.get('user').commentlikes_set.all().values_list('comment__pk', flat=True):
            return True
        else:
            return False


class BlogPostSerializer(serializers.ModelSerializer):
    # comments = CommentViewSerializer(many=True, read_only=True)
    author_username = serializers.ReadOnlyField(source='author.username', read_only=True)
    author_image = serializers.ImageField(source='author.profile.image', read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted', 'author_username', 'author_image', 'is_liked']
        extra_kwargs = {'date_posted': {'read_only': True}}

    def get_is_liked(self, obj):
        if obj.pk in self.context.get('user').postlikes_set.all().values_list('post__pk', flat=True):
            return True
        else:
            return False


class NotificationSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['notification_text', 'url']

    def get_url(self, obj):
        if obj.post:
            return reverse('post-detail', kwargs={'pk': obj.post.pk})
        elif obj.comment:
            return reverse('post-detail'+'?cpk='+str(obj.comment.pk), kwargs={'pk': obj.comment__post.pk})
        else:
            return reverse('post-detail'+'?ccpk='+str(obj.child_comment.pk), kwargs={'pk': obj.child_comment__post.pk})
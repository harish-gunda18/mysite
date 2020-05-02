from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from blog.models import Comment, Notification, ChildComment, PostLikes, CommentLikes, ChildCommentLikes


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Comment)
def create_parent_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(notification_text=instance.author.username + ' has commented on your post',
                                    post=instance.post, author=instance.post.author, comment=instance)


@receiver(post_save, sender=ChildComment)
def create_child_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(notification_text=instance.author.username + ' has replied to your comment',
                                    post=instance.post, author=instance.parent_comment.author, child_comment=instance)


@receiver(post_save, sender=PostLikes)
def create_post_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(notification_text=instance.author.username + ' has liked your post',
                                    post=instance.post, author=instance.post.author, liked_post=instance)


@receiver(post_save, sender=CommentLikes)
def create_comment_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(notification_text=instance.author.username + ' has liked your comment',
                                    comment=instance.comment, author=instance.comment.author,
                                    post=instance.comment.post, liked_comment=instance)


@receiver(post_save, sender=ChildCommentLikes)
def create_child_comment_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(notification_text=instance.author.username + ' has liked your comment',
                                    author=instance.child_comment.author, child_comment=instance.child_comment,
                                    post=instance.child_comment.post, liked_child_comment=instance)

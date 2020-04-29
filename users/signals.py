from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from blog.models import Comment, Notification, ChildComment


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
        notif = Notification(notification_text=instance.author.username + ' has commented on your post', post=instance.post,
                             author=instance.post.author, comment=instance)
        notif.save()


@receiver(post_save, sender=ChildComment)
def create_child_comment_notification(sender, instance, created, **kwargs):
    if created:
        notif = Notification(notification_text=instance.author.username + ' has replied to your comment', post=instance.post,
                             author=instance.parent_comment.author, child_comment=instance)
        notif.save()

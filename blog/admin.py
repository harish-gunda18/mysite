from django.contrib import admin


# Register your models here.


from .models import Post, Comment, ChildComment, Notification, PostLikes, CommentLikes, ChildCommentLikes
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ChildComment)
admin.site.register(Notification)
admin.site.register(PostLikes)
admin.site.register(CommentLikes)
admin.site.register(ChildCommentLikes)

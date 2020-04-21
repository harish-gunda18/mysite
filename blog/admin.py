from django.contrib import admin


# Register your models here.


from .models import Post, Comment, ChildComment
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ChildComment)

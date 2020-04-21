from django.forms import ModelForm, Textarea
from blog.models import Comment, ChildComment


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class ChildCommentCreateForm(ModelForm):
    class Meta:
        model = ChildComment
        fields = ['comment_text']

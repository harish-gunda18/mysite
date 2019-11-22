from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from django.contrib.auth.models import User
from blog.models import Post
from blog.api.serializers import BlogPostSerializer


@api_view(['GET'])
def api_detail_post_view(request, title):
    try:
        # title = title.replace(r'%20', ' ')
        blog_post = Post.objects.get(title=title)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

"""
@api_view(['PUT'])
def api_detail_post_view(request, title):
    try:
        blog_post = Stock.objects.get(title=title)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogPostSerializer(blog_post, date = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_detail_post_view(request, ticker):
    try:
        blog_post = Post.objects.get(ticker=ticker)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            serializer.save()
            data["success"] = 'delete successful'
        else:
            data["success"] = 'delete successful'
        return Response(data=data)


@api_view(['POST'])
def api_detail_post_view(request, ticker):
    user = User.objects.get(pk=1)
    blog_post =
"""


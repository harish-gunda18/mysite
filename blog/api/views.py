from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter

# from django.contrib.auth.models import User
from blog.models import Post
from blog.api.serializers import BlogPostSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_detail_post_view(request, title):
    try:
        title = title.replace(r'%20', ' ')
        blog_post = Post.objects.get(title=title)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def api_update_post_view(request, title):
    try:
        title = title.replace(r'%20', ' ')
        blog_post = Post.objects.get(title=title)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if blog_post.author != request.user:
        return Response({"response": "You don't have permission to edit that"})

    if request.method == 'PUT':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_delete_post_view(request, title):
    try:
        title = title.replace(r'%20', ' ')
        blog_post = Post.objects.get(title=title)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if blog_post.author != request.user:
        return Response({"response": "You don't have permission to delete that"})

    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data["success"] = 'delete successful'
        else:
            data["failure"] = 'delete failed'
        return Response(data=data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def api_create_post_view(request):
    user = request.user
    blog_post = Post(author=user)
    if request.method == 'POST':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiPostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'content')

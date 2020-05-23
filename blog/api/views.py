from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from blog.models import Post
from blog.api.serializers import BlogPostSerializer, NotificationSerializer


# view to get post details like title,content,date_posted,author,image,is_liked
@api_view(['GET'])  # ensure only get method
@permission_classes((IsAuthenticated,))  # only authenticated can get these details
def api_detail_post_view(request, pk):
    try:
        blog_post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BlogPostSerializer(blog_post, context={'user': request.user})
    return Response(serializer.data)


# view to update post details like title,content
@api_view(['PUT'])  # ensure only put method
@permission_classes((IsAuthenticated,))  # only authenticated can get these details
def api_update_post_view(request, pk):
    try:
        blog_post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if blog_post.author != request.user:
        return Response({"response": "You don't have permission to edit that"})

    serializer = BlogPostSerializer(blog_post, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = 'update successful'
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to delete post
@api_view(['DELETE'])  # ensure only delete method
@permission_classes((IsAuthenticated,))  # only authenticated can delete post
def api_delete_post_view(request, pk):
    try:
        blog_post = Post.objects.get(pk=pk)
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


# view to create post
@api_view(['POST'])  # ensure only post method
@permission_classes((IsAuthenticated,))  # only authenticated can create new post
def api_create_post_view(request):
    user = request.user
    blog_post = Post(author=user)
    if request.method == 'POST':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to search post details like title,content which is class based api view
class ApiPostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'content')


class ApiNotificationListView(ListAPIView):
    serializer_class = NotificationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'content')

    def get_queryset(self):
        return self.request.user.notification_set.all().order_by('-date_posted')

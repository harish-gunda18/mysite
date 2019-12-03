from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import RegistrationSerializer, UserPropertiesSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def api_user_add_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered new user'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except account.DoesnotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserPropertiesSerializer(account)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def account_update_view(request):
    try:
        account = request.user
    except account.DoesnotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = UserPropertiesSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "Successfully updated account"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
@api_view(['PUT'])
def api_update_post_view(request, title):
    try:
        title = title.replace(r'%20', ' ')
        blog_post = Post.objects.get(title=title)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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

    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data["success"] = 'delete successful'
        else:
            data["failure"] = 'delete failed'
        return Response(data=data)


@api_view(['POST'])
def api_create_post_view(request):
    user = User.objects.get(pk=1)
    blog_post = Post(author=user)
    if request.method == 'POST':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

from users.api.views import api_user_add_view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users'

urlpatterns = [
    path('register/', api_user_add_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
]

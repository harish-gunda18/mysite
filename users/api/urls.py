from users.api.views import api_user_add_view
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('register/', api_user_add_view, name='register')
]

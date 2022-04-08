from atexit import register
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    # path('login/', CreateUserView.as_view()),
]
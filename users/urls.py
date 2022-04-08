from django.urls import path
from .views import *

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('obtain-token/', ObtainTokenView.as_view(), name='obtain-token'),
    path('create-status/', CreateStatusView.as_view(), name='create-status'),
]
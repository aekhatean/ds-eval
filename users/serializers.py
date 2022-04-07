from rest_framework import serializers
from .models import ExtendedUser


class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        exclude = ('is_active', 'is_staff',)
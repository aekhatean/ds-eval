import email
from rest_framework import serializers
from .models import ExtendedUser


class ExtendedUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
        
    def create(self, validated_data):
    
        user = ExtendedUser.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            country_code=validated_data['country_code'],
            phone_number=validated_data['phone_number'],
            gender=validated_data['gender'],
            birthdate=validated_data['birthdate'],
            avatar=validated_data['avatar'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user
    class Meta:
        model = ExtendedUser
        fields = (
            'id', 'first_name', 'last_name', 'country_code', 'phone_number', 'gender', 'birthdate', 'avatar', 'email', 'password',
        )
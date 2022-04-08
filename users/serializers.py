from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import ExtendedUser, Status


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
        
        
class TokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        write_only=True
    )
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        read_only=True
    )

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(request=self.context.get('request'),
                                phone_number=phone_number, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "Phone_number" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
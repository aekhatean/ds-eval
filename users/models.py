from datetime import datetime
import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError


## Utilities go here

# Validate birthdate is in the past
def validate_birthdate(in_date):
    comparable_in_date = datetime.strptime(str(in_date), "%Y-%m-%d").date()
    present_date = datetime.now().date()
    if comparable_in_date > present_date:
        raise ValidationError("Birthdate must be in the past")


# Validate entered phone number is a valid E.164
def validate_phone_e164(number):
    if not re.match(r"^\+?[1-9]\d{1,14}$", number):
        raise ValidationError(
            ('%(number)s is not a valid phone number'),
            params={'number': number},
        )


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        first_name,
        last_name,
        country_code,
        phone_number,
        gender,
        birthdate,
        avatar,
        email,
        password,
        **other_fields):

        if not first_name:
            raise ValidationError('First name is required')
        
        if not last_name:
            raise ValidationError('Last name is required')
        
        if not phone_number:
            raise ValidationError('Phone number is required')
        
        # As validators do not run automatically unless used with a ModelForm
        validate_birthdate(birthdate)
        validate_phone_e164(phone_number)
        
        email = self.normalize_email(email)
        user = self.model(
                email=email,
                first_name=first_name,
                last_name=last_name,
                country_code=country_code,
                phone_number=phone_number,
                gender=gender,
                birthdate=birthdate,
                avatar=avatar,
                **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self,
        first_name,
        last_name,
        country_code,
        phone_number,
        gender,
        birthdate,
        avatar,
        email,
        password,
        **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be have is_staff=True')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be have is_superuser=True')
        
        return self.create_user(
            first_name,
            last_name,
            country_code,
            phone_number,
            gender,
            birthdate,
            avatar,
            email,
            password,
            **other_fields)


class ExtendedUser(AbstractBaseUser, PermissionsMixin):
    genders = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    country_codes = [
        ("eg", "EG"),
        ("us", "US"),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=2, choices=country_codes)
    phone_number = models.CharField(max_length=15, validators=[validate_phone_e164], unique=True)
    gender = models.CharField(max_length=6, choices=genders, default="male")
    birthdate = models.DateField(validators=[validate_birthdate])
    avatar = models.ImageField()
    email = models.EmailField(blank=True, default='', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # Use new User manager for the extended user
    objects = CustomUserManager()
    
    # User login (get a token) with phone number
    USERNAME_FIELD = 'phone_number'
    
    # fields required while creating a superuser
    REQUIRED_FIELDS = ['first_name', 'last_name', 'country_code', 'gender', 'birthdate', 'avatar', 'email']
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
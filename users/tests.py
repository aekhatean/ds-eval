from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class CustomUserTests(TestCase):
    def test_validate_birthdate(self):
        db = get_user_model()
        with self.assertRaises(ValidationError):
            db.objects.create_user(
                first_name='Adham',
                last_name='Khatean',
                country_code='eg',
                phone_number='+2010203040',
                gender='male',
                birthdate='2100-04-08',
                avatar='path/to/avatar.png',
                email='adham3000@email.com',
                password='a4s3d2f1')
            
            
    def test_validate_phone_e164(self):
        db = get_user_model()
        with self.assertRaises(ValidationError):
            db.objects.create_user(
                first_name='Adham',
                last_name='Khatean',
                country_code='eg',
                phone_number='',
                gender='male',
                birthdate='2022-04-08',
                avatar='path/to/avatar.png',
                email='adham3000@email.com',
                password='a4s3d2f1')
    
        with self.assertRaises(ValidationError):
            db.objects.create_user(
                first_name='Adham',
                last_name='Khatean',
                country_code='eg',
                phone_number='dasdfd',
                gender='male',
                birthdate='2022-04-08',
                avatar='path/to/avatar.png',
                email='adham3000@email.com',
                password='a4s3d2f1')
    
        with self.assertRaises(ValidationError):
            db.objects.create_user(
                first_name='Adham',
                last_name='Khatean',
                country_code='eg',
                phone_number='+123456789123456798',
                gender='male',
                birthdate='2022-04-08',
                avatar='path/to/avatar.png',
                email='adham3000@email.com',
                password='a4s3d2f1')
    
    
    def test_create_user(self):
        db = get_user_model()
        new_user = db.objects.create_user(
            'Adham',
            'Khatean',
            'eg',
            '+2010203040',
            'male',
            '2022-04-08',
            'path/to/avatar.png',
            'adham@email.com',
            'a4s3d2f1')
        self.assertEqual(new_user.first_name, 'Adham')
        self.assertEqual(new_user.last_name, 'Khatean')
        self.assertEqual(new_user.country_code, 'eg')
        self.assertEqual(new_user.phone_number, '+2010203040')
        self.assertEqual(new_user.gender, 'male')
        self.assertEqual(new_user.birthdate, '2022-04-08')
        self.assertEqual(new_user.email, 'adham@email.com')
        self.assertFalse(new_user.is_superuser)
        self.assertFalse(new_user.is_staff)
        self.assertTrue(new_user.is_active)
        self.assertEqual(str(new_user), 'Adham Khatean')
        with self.assertRaises(ValidationError):
            db.objects.create_user(
            first_name='Adham',
            last_name='Khatean',
            country_code='eg',
            phone_number='',
            gender='male',
            birthdate='2022-04-08',
            avatar='path/to/avatar.png',
            email='adham2@email.com',
            password='a4s3d2f1')
            
        with self.assertRaises(ValidationError):
            db.objects.create_user(
            first_name='',
            last_name='Khatean',
            country_code='eg',
            phone_number='',
            gender='male',
            birthdate='2022-04-08',
            avatar='path/to/avatar.png',
            email='adham2@email.com',
            password='a4s3d2f1')
            
        with self.assertRaises(ValidationError):
            db.objects.create_user(
            first_name='Adham',
            last_name='',
            country_code='eg',
            phone_number='',
            gender='male',
            birthdate='2022-04-08',
            avatar='path/to/avatar.png',
            email='adham2@email.com',
            password='a4s3d2f1')
    
    
    def test_create_superuser(self):
        db = get_user_model()
        new_superuser = db.objects.create_superuser(
            'Adham',
            'Khatean',
            'eg',
            '+2010203070',
            'male',
            '2022-04-08',
            'path/to/avatar.png',
            'super@email.com',
            'a4s3d2f1')
        self.assertEqual(new_superuser.first_name, 'Adham')
        self.assertEqual(new_superuser.last_name, 'Khatean')
        self.assertEqual(new_superuser.country_code, 'eg')
        self.assertEqual(new_superuser.phone_number, '+2010203070')
        self.assertEqual(new_superuser.gender, 'male')
        self.assertEqual(new_superuser.birthdate, '2022-04-08')
        self.assertEqual(new_superuser.email, 'super@email.com')
        self.assertTrue(new_superuser.is_superuser)
        self.assertTrue(new_superuser.is_staff)
        self.assertTrue(new_superuser.is_active)
        self.assertEqual(str(new_superuser), 'Adham Khatean')
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
            first_name='Adham',
            last_name='Khatean',
            country_code='eg',
            phone_number='+2010204060',
            gender='male',
            birthdate='2022-04-08',
            avatar='path/to/avatar.png',
            email='super2@email.com',
            password='a4s3d2f1',
            is_superuser=False)
            
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
            first_name='Adham',
            last_name='Khatean',
            country_code='eg',
            phone_number='+2010203080',
            gender='male',
            birthdate='2022-04-08',
            avatar='path/to/avatar.png',
            email='super3@email.com',
            password='a4s3d2f1',
            is_staff=False)

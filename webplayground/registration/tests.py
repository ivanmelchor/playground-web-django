from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
# Este test nos permite verificar que se creó el perfil del usuario registrado
# Ejecutamos "python manage.py test registration"
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)

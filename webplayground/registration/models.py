from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

# Optimiza el espacio utilizado por las imagenes de avatar
# Elimina el avatar anterior siempre que se actualiza
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Modelo de Perfil de usuario (Instancia)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200,null=True, blank=True)

    class Meta:
        # Ordena a partir del nombre de usuario haciendo referencia al Usuario
        ordering = ['user__username'] 

# Método que asegura y crea un Perfil para la instancia de Usuario cuando es creado un Usuario
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
       # print("Se acaba de crear un usuario y su perfil enlazado")
        
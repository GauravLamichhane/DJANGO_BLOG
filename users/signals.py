from django.db.models.signals import post_save#this signals gets fired after and object is saved
from django.contrib.auth.models import User#built in user module and is sender
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender = User)#decorator 
def create_profile(sender,instance,created,**kwargs):
  if created:
    Profile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_profile(sender,instance,**kwargs):
  instance.profile.save()
from django.db.models.signals import post_delete, post_save
from .models import User, Profile


#! When user created profile will be create automatically
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            email=user.username,
            name=user.first_name,
        )

#! When profile updated user will update automatically
def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.email
        user.save()

#! When profile deleted user will be delete automatically
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
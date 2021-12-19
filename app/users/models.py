from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    profile_image = models.ImageField(upload_to = "profiles/", default = "profiles/avatar.svg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.name} --> {self.email} --> {datetime.datetime.strftime(self.created, "%d-%B-%Y %A")}'



class Skill(models.Model):
    SKILL_BADGE_COLORS = [
        ('bg-primary','Blue'),
        ('bg-secondary','Grey'),
        ('bg-success','Green'),
        ('bg-danger','Red'),
        ('bg-warning ','Yellow'),
        ('bg-info','Turquoise')
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    badge_color = models.CharField(max_length=200, choices=SKILL_BADGE_COLORS, default="bg-primary" , null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.owner.name} --> {self.name}'
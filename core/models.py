from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    file = models.ImageField(upload_to="images")

class Sport(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    thumbnail = models.OneToOneField(Image, on_delete=models.CASCADE)

class Player(models.Model):
    first_name = models.TextField()
    pseudonym = models.CharField(max_length=10, primary_key=True)
    last_name = models.TextField()
    birthday = models.DateField()
    sports = models.ManyToManyField(Sport, related_name="players")
    phone_number = models.TextField(unique=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="profile")

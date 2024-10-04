from django.db import models
from core.models import *

class Team(models.Model):
    teamid = models.AutoField(primary_key=True)
    team_name = models.TextField()
    team_logo = models.ForeignKey(Image, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player, related_name="team") #Maximum of 16 players

class Match(models.Model):
    sport = models.OneToOneField(Sport, on_delete=models.CASCADE, related_name="match")
    teams = models.ManyToManyField(Team, related_name="match") #Maximum of 2 teams
    time = models.DateTimeField()
    venue = models.TextField()
    arena = models.TextField()

class Events(models.Model):
    eventid = models.AutoField(primary_key=True)
    team = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="event")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="event")
    assist = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="assist")
    time = models.DateTimeField(auto_now=True)
    time_on_clock = models.TextField()
    event = models.TextField()

    def number_of_shots(self):
        return Events.objects.filter(event="shot").count()

class Score(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="score")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="score")
    score = models.IntegerField()

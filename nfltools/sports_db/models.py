from django.db import models


class Leagues(models.Model):
    league_name = models.CharField(max_length=100)
    league_id = models.IntegerField()
    sport = models.CharField(max_length=100)
    alt_league_name = models.CharField(max_length=200, default=None, blank=True, null=True)


class Teams(models.Model):
    team_name = models.CharField(max_length=100)
    team_id = models.IntegerField()
    short_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    alt_team_name = models.CharField(max_length=200, default=None, blank=True, null=True)
    team_league_id = models.IntegerField()
    league = models.ForeignKey('Leagues', on_delete=models.CASCADE, default=None)


class Players(models.Model):
    player_name = models.CharField(max_length=100)
    player_id = models.IntegerField()
    birthday = models.DateField()
    position = models.CharField(max_length=30)
    sport = models.CharField(max_length=30)
    college = models.CharField(max_length=100, blank=True, null=True)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    current_id = models.IntegerField()
    current_team = models.ForeignKey('Teams', on_delete=models.CASCADE, default=None)
    #year here or different table?


class Seasons(models.Model):
    season_id = models.CharField(max_length=10)
    league = models.ForeignKey('Leagues', on_delete=models.CASCADE, default=None)


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_id = models.IntegerField()
    event_date = models.DateField()
    event_time = models.TimeField(default=None)
    sport = models.CharField(max_length=30)
    season = models.ForeignKey('Seasons', on_delete=models.CASCADE, default=None)
    home_team = models.ForeignKey('Teams', on_delete=models.CASCADE, default=None, related_name="home")
    away_team = models.ForeignKey('Teams', on_delete=models.CASCADE, default=None, related_name="away")
    home_score = models.CharField(max_length=25, default=0)
    away_score = models.CharField(max_length=25, default=0)
    result = models.ForeignKey('Teams', on_delete=models.CASCADE, default=None, related_name="winner") #None = tie where appropriate

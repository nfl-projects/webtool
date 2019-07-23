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
    college = models.CharField(max_length=100)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    current_id = models.IntegerField()
    current_team = models.ForeignKey('Teams', on_delete=models.CASCADE, default=None)


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_id = models.IntegerField()
    event_date = models.CharField(max_length=250)
    season_id = models.IntegerField()
import requests
import pprint
import json


from django.conf import settings
from django.db import transaction
from sports_db.models import Teams, Players, Events, Leagues


class SDBProvider:
    def __init__(self):
        self.key = settings.SPORTS_DB_API
        self.base = 'https://www.thesportsdb.com/api/v1/json/'
        self.type = None #league, event, team or player

    
    def get_league_by_id(self,league_id):
        return(Leagues.objects.get(league_id=league_id))


    def get_team_by_id(self,team_id):
        return(Teams.objects.get(team_id=team_id))

    
    def get_player_by_id(self,player_id):
        return(Players.objects.get(player_id=player_id))

    
    def load_all_leagues(self):
        already_leagues = Leagues.objects.all().values_list('league_id',flat=True)
        
        url = f'{self.base}{self.key}/all_leagues.php'
        
        response = requests.get(url)
        
        with transaction.atomic():
            if response.json()['leagues'] and type(response.json()['leagues']) is list:
                for league in response.json()['leagues']:
                    if int(league['idLeague']) not in already_leagues:
                        new_league = Leagues(league_name=league['strLeague'],
                                            league_id=league['idLeague'],
                                            sport=league['strSport'],
                                            alt_league_name=league['strLeagueAlternate'])
                        new_league.save()

    
    def load_all_teams_in_league(self, league_id):
        league_object = self.get_league_by_id(league_id)
        already_teams = Teams.objects.all().values_list('team_id',flat=True)

        url = f'{self.base}{self.key}/lookup_all_teams.php?id={league_id}'

        response = requests.get(url)
        
        with transaction.atomic():
            if response.json()['teams'] and type(response.json()['teams']) is list:
                for team in response.json()['teams']:
                    if int(team['idTeam']) not in already_teams:
                        new_team = Teams(team_name=team['strTeam'],
                                        team_id=team['idTeam'],
                                        short_name=team['strTeamShort'],
                                        alt_team_name=team['strAlternate'],
                                        team_league_id=team['idLeague'],
                                        league=league_object)
                        new_team.save()

    
    def load_players_by_team(self, team_id):
        team_object = self.get_team_by_id(team_id)
        #already_players = Players.objects.all().values_list('player_id','current_id',flat=True)
        #already_players = Players.objects.all()

        url = f'{self.base}{self.key}/lookup_all_players.php?id={team_id}'

        response = requests.get(url)
        
        with transaction.atomic():
            if response.json()['player'] and type(response.json()['player']) is list:
                for player in response.json()['player']:
                    if int(player['idPlayer']) in already_players:
                        if int(player['idPlayer']) 

        
        
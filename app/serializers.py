from rest_framework import serializers
from  .models import Team, Player, Game, Standing

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'team_id', 
            'city', 
            'full_name', 
            'nick_name', 
            'logo', 
            'short_name', 
            'conf_name', 
            'div_name'
        ]

class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.short_name', read_only=True)

    class Meta:
        model = Player
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'team_name',
            'years_pro', 
            'college_name', 
            'country', 
            'dob', 
            'affiliation', 
            'height_in_meters',
            'weight_in_kilograms',
            'pos'
        ]

class GameSerializer(serializers.ModelSerializer):
    home = serializers.CharField(source='team.home_team', read_only=True)
    away = serializers.CharField(source='team.away_team', read_only=True)

    class Meta:
        model = Game
        fields = [
            'game_id',
            'home',
            'away',
            'date_time',
            'home_score',
            'away_score'
        ]

class StandingSerializer(serializers.ModelSerializer):
    team = serializers.CharField(source='team.short_name', read_only=True)
    
    class Meta:
        model = Standing
        fields = [
            'team',
            'win',
            'loss',
            'conference',
            'conference_rank',
            'division',
            'division_rank'
        ]
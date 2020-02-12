from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Game, Player, Standing, Team

def index(request):
    return render(request, 'stats/index.html')

def player(request, player_id):
    return render(request, 'players/player.html')

def players(request):
    guards = Player.objects.filter(pos='G')
    guard_forwards = Player.objects.filter(pos='G-F')
    forwards = Player.objects.filter(pos='F')
    centers = Player.objects.filter(pos='C')
    forward_centers = Player.objects.filter(pos='F-C')

    context = {
        'positions' : {
            'Guards': guards,
            'Guard Forwards': guard_forwards,
            'Forwards': forwards,
            'Centers': centers,
            'Forward Centers': forward_centers
        }
    }

    return render(request, 'players/index.html', context)

def news(request):
    return render(request, 'stats/news.html')

def schedule(request):
    return render(request, 'stats/schedule.html')

def scores(request):
    scores = Game.objects.all()
    context = {
        'scores': scores
    }
    return render(request, 'stats/scores.html', context)

def standing(request):
    western = Standing.objects.filter(conference = 'west').order_by('-win')
    eastern = Standing.objects.filter(conference = 'east').order_by('-win')
    context = {
        'conferences': {
            'western': western,
            'eastern': eastern
        }
        
    }
    return render(request, 'stats/standing.html', context)

def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    context = {
        'team': team
    }
    return render(request, 'teams/team.html', context)

def teams(request):
    team_list = Team.objects.all()
    context = {
        'team_list': team_list
    }
    return render(request, 'teams/index.html', context)


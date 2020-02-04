from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Player, Team

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
        'guards': guards,
        'guard_forwards': guard_forwards,
        'forwards': forwards,
        'centers': centers,
        'forward_centers': forward_centers
    }
    
    return render(request, 'players/index.html', context)

def news(request):
    return render(request, 'stats/news.html')

def schedule(request):
    return render(request, 'stats/schedule.html')

def scores(request):
    return render (request, 'stats/scores.html')

def standing(request):
    return render(request, 'stats/standing.html')

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


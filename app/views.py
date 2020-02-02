from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Player, Team

# Create your views here.
def index(request):
    return HttpResponse("HoopFrance index.")

def player(request, player_id):
    return HttpResponse("HoopFrance single_team.")

def players(request):
    return HttpResponse("HoopFrance players.")

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


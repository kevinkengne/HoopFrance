from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Game, Player, Standing, Team
from .serializers import TeamSerializer, GameSerializer, PlayerSerializer, StandingSerializer
from .api.duels import load_duels

def index(request):
    return render(request, 'stats/index.html')

def player(request, player_id):
    if request.method == 'GET':
        player = get_object_or_404(Player, pk=player_id)
        serializer = PlayerSerializer(player, many=False)
    return JsonResponse(serializer.data, safe=False)

def players(request):
    if request.method == 'GET':
        players = Player.objects.all()
        position = request.GET.get('pos', None)
        if position is not None:
            players = players.filter(pos=position)
        serializer = PlayerSerializer(players, many=True)
    return JsonResponse(serializer.data, safe=False)

def news(request):
    return render(request, 'stats/news.html')

def duels(request):
    duels = load_duels()
    context = {
        'duels': duels
    }
    return render(request, 'stats/duels.html', context)

def scores(request):
    scores = Game.objects.all()
    serializer = GameSerializer(scores, many=True)
    return JsonResponse(serializer.data, safe=False)

def standing(request):
    if request.method == 'GET':
        standing = Standing.objects.all()
        conference = request.GET.get('conference', None)
        if conference == 'west':
            standing = standing.filter(conference = 'west').order_by('-win')
        elif conference == 'east':
            standing = standing.filter(conference = 'east').order_by('-win')
        serializer = StandingSerializer(standing, many=True)
        return JsonResponse(serializer.data, safe=False)

def team(request, team_id):
    if request.method == 'GET':
        team = get_object_or_404(Team, pk=team_id)
        serializer = TeamSerializer(team, many=False)
    return JsonResponse(serializer.data, safe=False)

def teams(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
    return JsonResponse(serializer.data, safe=False)


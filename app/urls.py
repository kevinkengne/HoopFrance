from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news', views.news, name='news'),
    path('players', views.players, name='players'),
    path('players/<int:player_id>', views.player, name='player'),
    path('schedule', views.schedule, name='schedule'),
    path('scores', views.scores, name='scores'),
    path('standing', views.standing, name='standing'),
    path('teams', views.teams, name='teams'),
    path('teams/<int:team_id>', views.team, name='team'),
]
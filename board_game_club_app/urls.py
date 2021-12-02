"""Defines URL patterns for board_game_club_app."""

from django.urls import path
from . import views

app_name = "board_game_club_app"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all board games
    path("boardgames/", views.boardgames, name="boardgames"),
    # Detail page for a single board game
    path("boardgames/<int:boardgame_id>/", views.boardgame, name="boardgame"),
]

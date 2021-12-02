"""Defines URL patterns for board_game_club_app."""

from django.urls import path
from . import views

app_name = "board_game_club_app"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
]

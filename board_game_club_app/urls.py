"""Defines URL patterns for board_game_club_app."""

from django.urls import path
from . import views

app_name = "board_game_club_app"
urlpatterns = [
    # Home page
    path("", views.index, name = "index"),
    # Page that shows all board games
    path("boardgames/", views.boardgames, name = "boardgames"),
    # Detail page for a single board game
    path("boardgames/<int:boardgame_id>/", views.boardgame, name = "boardgame"),
    # Page for adding a new review
    path('new_review/<int:review_id>/', views.new_review, name = 'new_review'),
    # Page for editing a review
    path('edit_review/<int:review_id>/', views.edit_review, name = 'edit_review'),
]

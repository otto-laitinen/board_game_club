from django.shortcuts import render
from .models import BoardGame


def index(request):
    """Board Game Club home page"""
    return render(request, "board_game_club_app/index.html")


def boardgames(request):
    """Shows all board games."""
    # Orders the board games by name (alphabetically):
    boardgames = BoardGame.objects.order_by("name")
    context = {"boardgames": boardgames}
    return render(request, "board_game_club_app/boardgames.html", context)

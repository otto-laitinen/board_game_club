from django.shortcuts import render


def index(request):
    """Board Game Club home page"""
    return render(request, "board_game_club_app/index.html")

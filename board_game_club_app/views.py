from django.shortcuts import render, redirect
from .models import BoardGame
from .forms import BoardGameForm


def index(request):
    """Board Game Club home page"""
    return render(request, "board_game_club_app/index.html")


def boardgames(request):
    """Shows all board games."""
    # Orders the board games by name (alphabetically):
    boardgames = BoardGame.objects.order_by("name")
    context = {"boardgames": boardgames}
    return render(request, "board_game_club_app/boardgames.html", context)


def boardgame(request, boardgame_id):
    """Shows a single board game and its information."""
    boardgame = BoardGame.objects.get(id=boardgame_id)
    reviews = boardgame.review_set.order_by("-date_added")
    context = {"boardgame": boardgame, "reviews": reviews}
    return render(request, "board_game_club_app/boardgame.html", context)
    

def new_board_game(request):
    """Add a new board game."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BoardGameForm()
    else:
        # POST data submitted; process data.
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_club_app:boardgames')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'board_game_club_app/new_board_game.html', context)

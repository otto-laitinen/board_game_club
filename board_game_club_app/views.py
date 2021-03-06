from django.shortcuts import render, redirect
from .models import BoardGame, Review
from .forms import BoardGameForm, ReviewForm, BorrowForm, BorrowedForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Board Game Club home page"""
    return render(request, "board_game_club_app/index.html")


@login_required
def boardgames(request):
    """Shows all board games."""
    # Orders the board games alphabetically (for clarity):
    boardgames = BoardGame.objects.order_by("name")
    context = {"boardgames": boardgames}
    return render(request, "board_game_club_app/boardgames.html", context)


@login_required
def boardgame(request, boardgame_id):
    """Shows a single board game and its information."""
    boardgame = BoardGame.objects.get(id=boardgame_id)
    description = BoardGame.description
    # We don't want to raise an error here. The user is only requesting to see a specific boardgame.
    # if boardgame.owner != request.user:
    #    raise Http404
    reviews = boardgame.review_set.order_by("-date_added")
    context = {"boardgame": boardgame, "reviews": reviews, "description": description}
    return render(request, "board_game_club_app/boardgame.html", context)


@login_required
def new_board_game(request):
    """Add a new board game."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = BoardGameForm()
    else:
        # POST data submitted; process data.
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            new_board_game = form.save(commit=False)
            new_board_game.owner = request.user
            new_board_game.save()
            form.save()
            return redirect("board_game_club_app:boardgames")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "board_game_club_app/new_board_game.html", context)


@login_required
def new_review(request, boardgame_id):
    """Add a new review for a particular board game."""
    boardgame = BoardGame.objects.get(id=boardgame_id)
    #boardgame = boardgame.objects.filter(owner=request.user).order_by('date_added')

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = ReviewForm()
    else:
        # POST data submitted; process data.
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.boardgame = boardgame
            new_review.save()
            return redirect("board_game_club_app:boardgame", boardgame_id=boardgame_id)
    # Display a blank or invalid form.
    context = {"boardgame": boardgame, "form": form}
    return render(request, "board_game_club_app/new_review.html", context)


@login_required
def edit_review(request, review_id):
    """Edit an existing review."""
    review = Review.objects.get(id=review_id)
    boardgame = review.boardgame

    #### This line cause the error in edit_review, when the review is not of a board game the user has created. ####
    #if boardgame.owner != request.user:
    #    raise Http404

    if request.method != "POST":
        # Initial request; pre-fill form with the current review.
        form = ReviewForm(instance=review)
    else:
        # POST data submitted; process data.
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("board_game_club_app:boardgame", boardgame_id=boardgame.id)
    context = {"review": review, "boardgame": boardgame, "form": form}
    return render(request, "board_game_club_app/edit_review.html", context)


@login_required
def borrow_game(request, boardgame_id):
    """Allow the user to borrow the game."""
    boardgame = BoardGame.objects.get(id=boardgame_id)
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = BorrowedForm()
    else:
        # POST data submitted; process data.
        form = BorrowedForm(data=request.post) ## form = BorrowForm(something that will save the data of available)
        BoardGame.available = False
        if form.is_valid():
            BoardGame.available = False
            form.save()
        #if form.is_valid():
        #    borrow_game = form.save(commit=False)
         #   borrow_game.boardgame = boardgame
          #  borrow_game.save()
           # return redirect("board_game_club_app:boardgame", boardgame_id=boardgame_id)

        context = {"available":BoardGame.available, "boardgame": boardgame, "form": form} 
        return render(request, "board_game_club_app/borrowed.html", context)

    context = {"available":BoardGame.available, "boardgame": boardgame, "form": form} 
    return render(request, "board_game_club_app/borrowed.html", context)

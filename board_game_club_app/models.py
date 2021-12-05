from django.db import models

class BoardGame(models.Model):
    """A board game and it's information."""

    name = models.CharField(max_length=150)
    description = models.TextField(
        max_length=400, null=True, help_text="Enter a short description of the game"
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.name


class Review(models.Model):
    """A review of a board game."""

    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    my_review = models.TextField(max_length=250)

    # Choices for choosing a rating for the game:
    CHOICES = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )

    rating = models.CharField(max_length=3, choices=CHOICES, default="0")
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.my_review[:50]}. . ."

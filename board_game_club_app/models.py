from django.db import models


class BoardGame(models.Model):
    """A board game and it's information."""

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.name

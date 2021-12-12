from django import forms
from .models import BoardGame, Review


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ["name", "description"]
        labels = {"name": "Name of the board game", "description": "Description"}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["my_review", "rating"]
        labels = {"my_review": "Review", "rating": "Rating"}
        widgets = {"my_review": forms.Textarea(attrs={"cols": 80})}


###test
class BorrowForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ["available"]
        labels = {"available": "available"}

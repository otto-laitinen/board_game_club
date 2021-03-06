from django import forms
from .models import BoardGame, Review


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ["name", "description"]
        labels = {"name": "Name", "description": "Description"}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["my_review", "rating"]
        labels = {"my_review": "", "rating": "Rating"}
        widgets = {"my_review": forms.Textarea(attrs={"cols": 80})}

##We did not use this class
class BorrowForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ["available"]
        labels = {"available": "Available"}


class BorrowedForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ["name"]
        labels = {"name": "Name"}

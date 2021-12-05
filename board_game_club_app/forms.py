from django import forms

from .models import BoardGame, Review

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'description']
        labels = {} #'text': ''

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = []
        labels = {}#'text': 'Review:'
        widgets = {}#'text': forms.Textarea(attrs={'cols': 250})

        # Probably need to fill the brackets with meaningful vlues 

        


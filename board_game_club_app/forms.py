from django import forms
from .models import BoardGame, Review
class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['text']
        labels = {'text': ''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {'text': 'Review:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 250})}


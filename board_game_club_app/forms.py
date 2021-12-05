from django import forms
from .models import BoardGame

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = []
        labels = {}
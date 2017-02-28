# forms.py

from django import forms
from django.core.exceptions import ValidationError

from .models import CharacterAttributes

class CharacterForm(forms.ModelForm):

    class Meta:
        model = CharacterAttributes
        fields = ('name', 'gender')


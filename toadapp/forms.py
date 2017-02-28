# forms.py

from django import forms
from django.core.exceptions import ValidationError

class CharacterForm(forms.Form):
    name = forms.CharField(label='name', max_length=20)

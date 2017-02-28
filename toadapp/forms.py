# forms.py

from django import forms

class CharacterForm(forms.Form):
    name = forms.CharField(label='name', max_length=20)

from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse

from toadapp.models import CharacterAttributes
from toadapp.character import Character

def index(request):
    return render_to_response("toadapp/index.html", {})

def create_character(request):
    new_character = Character()
    return render_to_response("toadapp/create-character.html", {'new_character':new_character})

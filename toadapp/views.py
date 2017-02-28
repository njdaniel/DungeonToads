from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

from toadapp.models import CharacterAttributes
from toadapp.character import Character
from .forms import CharacterForm

def index(request):
    return render_to_response("toadapp/index.html", {})

def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        else:
            form = CharacterForm()
    return render(request, "toadapp/create_character.html", {'form':form})

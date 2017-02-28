from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

from toadapp.models import CharacterAttributes
from toadapp.character import Character
from .forms import CharacterForm

def index(request):
    return render_to_response("toadapp/index.html", {})

def create_character(request):
    print('in create_character')
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        print('form submitted')
        if form.is_valid():
            print('Form is valid')
            return HttpResponseRedirect('/thanks/')
    else:
        form = CharacterForm()
    return render_to_response("toadapp/create_character.html", {'form':form})

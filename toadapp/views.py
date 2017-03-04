from django.shortcuts import render, render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from toadapp.models import CharacterAttributes
from toadapp.character import Character
from .forms import CharacterForm
from .models import CharacterAttributes

def index(request):
    return render_to_response("toadapp/index.html", {})

def create_character(request):
    print('in create_character')
    print(request.method)
    if request.method == 'POST':
        print('inside post')
        form = CharacterForm(request.POST)
        print('form submitted')
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('character_detail', id=form.save().pk)
    else:
        form = CharacterForm()
    return render(request, "toadapp/create_character.html", {'form':form})

def character_detail(request, id):
    character = CharacterAttributes.objects.get(id=id)
    return render(request, "toadapp/character_detail.html", {"id":id, "character":character})

def character_list(request):
    characters = CharacterAttributes.objects.all()
    return render_to_response("toadapp/character_list.html", {'characters':characters})

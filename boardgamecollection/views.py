from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import Game

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games= Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

def game_index(request, cat_id):
    game= Game.objects.get(id=cat_id)
    return render(request, 'games/detail.html', { 'game': game })

class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url='/games/'

class GameUpdate(UpdateView):
    model = Game
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'
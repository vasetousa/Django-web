import math
from math import trunc

from django.shortcuts import render, redirect

# Create your views here.
from gamesplay.gamesplayweb.forms import CreateProfileForm, EditProfileForm, CreateGameForm, EditGameForm, \
    DeleteGameForm
from gamesplay.gamesplayweb.models import Profile, Game


def index(request):
    current_profile = get_profile()
    context = {
        'show_create_profile': True,
        'hide_bar': True,

    }

    if current_profile:
        return redirect('dashboard')
    context = {
        'show_create_profile': True,  # shows the 'create' profile tag
        'hide_bar': False,  # hides the bar (no profile)

    }
    return render(request, 'home-page.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

        context = {
            'form': form,
            'hide_bar': False,
            'show_create_profile': True,
        }

        return render(request, 'create-profile.html', context)


def profile_edit(request):
    current_profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_profile)

        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=current_profile)
        context = {
            'form': form,
            'hide_bar': True,
            'show_create_profile': False,
        }
        return render(request, 'edit-profile.html', context)


def profile_delete_confirm(request):
    return render(request, 'delete-profile.html')


def profile_delete(request):
    if request.method == 'POST':
        Profile.objects.all().delete()
        Game.objects.all().delete()
        return redirect('index')
    # else:
    #     context = {
    #         'hide_bar': True,
    #         'show_create_profile': False,
    #     }
    #
    #     return redirect('index')


def profile_details(request):
    current_profile = get_profile()
    current_games = get_games()
    if current_games:
        total_games = len(current_games)
        average_rating = f'{sum([t.rating for t in current_games]):.1f}'
    else:
        total_games = 0
        average_rating = 0

    context = {
        'current_profile': current_profile,
        'current_games': current_games,
        'show_create_profile': True,
        'hide_bar': True,
        'total_games': total_games,
        'average_rating': average_rating,

    }

    return render(request, 'details-profile.html', context)


def dashboard(request):
    current_profile = get_profile()
    current_games = get_games()
    if current_games:
        total_games = len(current_games)
        average_rating = f'{sum([t.rating for t in current_games]):.1f}'

    else:
        total_games = 0
        average_rating = 0

    context = {
        'current_profile': current_profile,
        'current_games': current_games,
        'show_create_profile': True,
        'hide_bar': True,
        'total_games': total_games,
        'average_rating': average_rating,

    }

    return render(request, 'dashboard.html', context)


def game_create(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = CreateGameForm()

        context = {
            "form": form,
            'show_create_profile': True,
            'hide_bar': True,
        }
        return render(request, 'create-game.html', context)


def game_edit(request, pk):
    current_game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, request.FILES, instance=current_game)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = EditGameForm(instance=current_game)

        context = {
            "form": form,
            'show_create_profile': True,
            'hide_bar': True,
        }
        return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    current_game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, request.FILES, instance=current_game)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = DeleteGameForm(instance=current_game)

        context = {
            "form": form,
            'show_create_profile': True,
            'hide_bar': True,
        }
        return render(request, 'delete-game.html', context)


def game_details(request, pk):
    current_game = Game.objects.get(pk=pk)
    context = {
        'show_create_profile': True,
        'hide_bar': True,
        'current_game': current_game,
    }
    return render(request, 'details-game.html', context)


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_games():
    games = Game.objects.all()
    if games:
        return games
    return None

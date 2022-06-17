from django.shortcuts import render, redirect

from online_music.music_app.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from online_music.music_app.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_albums():
    album = Album.objects.all()
    if album:
        return album
    return None


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
        context = {
            'form': form,
            'profile': None,
        }
        return render(request, 'home-no-profile.html', context)


def profile_details(request):
    total_albums = get_albums()
    if total_albums:
        total_albums = len(total_albums)
    else:
        total_albums = 0
    current_profile = get_profile()
    context = {
        'profile': current_profile,
        'albums': total_albums,
    }
    return render(request, 'profile-details.html', context)


def profile_delete_final():
    Profile.objects.all().delete()
    Album.objects.all().delete()
    return redirect('home page')


def profile_delete(request):
    if request.method == 'POST':
        return render(request, 'profile-delete.html')
    else:
        # form = DeleteProfileForm()
        # context = {
        #     'form': form,
        # }
        return redirect(profile_delete_final())


def home_page(request):
    current_profile = get_profile()
    if current_profile:
        context = {
            'profile': True,
            'albums': get_albums()
        }
        return render(request, 'home-with-profile.html', context)

    return redirect('profile create')


def album_add(request):
    current_profile = get_profile()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateAlbumForm()
        context = {
            'form': form,
            'profile': current_profile,
        }
        return render(request, 'add-album.html', context)


def album_details(request, pk):
    current_profile = get_profile()
    current_album = Album.objects.get(pk=pk)
    context = {
        'album': current_album,
        'profile': current_profile,
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    current_profile = get_profile()
    current_instance = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, request.FILES, instance=current_instance)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=current_instance)
        context = {
            'form': form,
            'profile': current_profile,
            'album': current_instance,
        }
        return render(request, 'edit-album.html', context)


def album_delete_final(request, pk):
    current_profile = get_profile()
    current_instance = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, request.FILES, instance=current_instance)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = EditAlbumForm(instance=current_instance)
    context = {
        'form': form,
        'profile': current_profile,
        'album': current_instance,
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    current_profile = get_profile()
    current_instance = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, request.FILES, instance=current_instance)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = DeleteAlbumForm(instance=current_instance)
    context = {
        'form': form,
        'profile': current_profile,
        'album': current_instance,
    }
    return render(request, 'delete-album.html', context)

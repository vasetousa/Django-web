from django.shortcuts import render, redirect

# Create your views here.
from online_notes.notes.forms import CreateNoteForm, EditNoteForm, DeleteNoteForm
from online_notes.notes.models import Profile, Note


def home_page(request):
    profile = get_profile()
    notes = get_notes()

    context = {
        'profile': profile,
        'notes': notes,
        'hide_add': False,
    }
    if profile:
        return render(request, 'home-with-profile.html', context)
    return render(request, 'home-no-profile.html', context)


def add_note(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateNoteForm()
        hide_add = True
        context = {
            'profile': profile,
            'form': form,
            'hide_add': hide_add,
        }
        return render(request, 'note-create.html', context)


def edit_note(request, pk):
    profile = get_profile()
    current_note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, request.FILES, instance=current_note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditNoteForm(instance=current_note)

        context = {
            'profile': profile,
            'notes': current_note,
            'hide_add': False,
            'form': form,
        }
        return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    profile = get_profile()
    current_note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, request.FILES, instance=current_note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteNoteForm(instance=current_note)

        context = {
            'profile': profile,
            'notes': current_note,
            'hide_add': False,
            'form': form
        }

        return render(request, 'note-delete.html', context)


def details_note(request, pk):
    profile = get_profile()
    current_note = Note.objects.get(pk=pk)

    context = {
        'profile': profile,
        'notes': current_note,
        'hide_add': False,
    }

    return render(request, 'note-details.html', context)


def profile(request):
    profile = get_profile()
    notes = get_notes()
    note_count = len(notes)

    context = {
        'profile': profile,
        'hide_add': False,
        'note_count': note_count,
    }
    return render(request, 'profile.html', context)


def profile_delete(request):
    profile = get_profile()
    all_notes = Note.objects.all()

    profile.delete()
    all_notes.delete()
    return redirect('home page')


def get_profile():
    current_profile = Profile.objects.all()
    if current_profile:
        return current_profile[0]
    return None


def get_notes():
    current_notes = Note.objects.all()
    if current_notes:
        return current_notes
    return None

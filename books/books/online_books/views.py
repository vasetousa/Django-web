# Create your views here.
from django.shortcuts import render, redirect

from books.online_books.forms import CreateProfileForm, AddBookPage, EditPageForm, EditProfileForm, DeleteProfileForm
from books.online_books.models import Profile, Book


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_books():
    books = Book.objects.all()
    if books:
        return books
    return None


def home_page(request):
    current_profile = get_profile()
    if not current_profile:
        return redirect('create profile page')
    current_books = get_books()
    context = {
        'current_profile': current_profile,
        'current_books': current_books,
    }
    return render(request, 'home-with-profile.html', context)


def add_book_page(request):
    current_profile = get_profile()
    if request.method == 'POST':
        form = AddBookPage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AddBookPage()
        context = {
            'form': form,
            'current_profile': current_profile,
        }
        return render(request, 'add-book.html', context)


def book_details_page(request, pk):
    current_profile = get_profile()
    current_book = Book.objects.get(pk=pk)
    context = {
        'current_book': current_book,
        'current_profile': current_profile,
    }
    return render(request, 'book-details.html', context)


def edit_book_page(request, pk):
    current_profile = get_profile()
    current_book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPageForm(request.POST, instance=current_book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditPageForm(instance=current_book)
        context = {
            'current_book': current_book,
            'current_profile': current_profile,
            'form': form,
        }
        return render(request, 'edit-book.html', context)


def delete_book_page(request, pk):
    current_book = Book.objects.get(pk=pk)
    current_book.delete()
    return redirect('create profile page')


def profile_page(request):
    current_profile = get_profile()
    context = {
        'current_profile': current_profile,

    }
    return render(request, 'profile.html', context)


def edit_profile_page(request):
    current_profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = EditProfileForm(instance=current_profile)
        context = {
            'current_profile': current_profile,
            'form': form,
        }
        return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    current_profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=current_profile)
        context = {
            'current_profile': current_profile,
            'form': form,
        }
        return render(request, 'delete-profile.html', context)


def create_profile_page(request):
    current_profile = get_profile()
    current_books = get_books()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'current_books': current_books,
        'current_profile': current_profile,
    }
    return render(request, 'home-no-profile.html', context)

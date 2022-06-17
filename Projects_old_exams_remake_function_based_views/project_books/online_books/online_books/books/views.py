# Create your views here.
from django.shortcuts import render, redirect

from online_books.books.forms import CreateProfileForm, AddBookForm, EditBookForm, EditProfileForm, DeleteProfileForm
from online_books.books.models import Profile, Book


def get_profile():
    current_profile = Profile.objects.all()
    if current_profile:
        return current_profile[0]
    return None


def get_books():
    current_books = Book.objects.all()
    if current_books:
        return current_books
    return None


def home_page(request):
    personal_profile = get_profile()
    current_books = get_books()

    if not personal_profile:
        return redirect('profile create')

    context = {
        'books': current_books,
        'profile': personal_profile,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-with-profile.html')
    else:

        form = AddBookForm()
        context = {
            'form': form,
            'profile': get_profile()
        }
        return render(request, 'add-book.html', context)


def edit_book(request, pk):
    current_book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = EditBookForm(request.POST, request.FILES, instance=current_book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditBookForm(instance=current_book)

        context = {
            'form': form,
            'profile': get_profile(),
        }
        return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    current_book = Book.objects.get(pk=pk)
    current_book.delete()
    return redirect('home page')


def book_details_page(request, pk):
    current_book = Book.objects.get(pk=pk)
    context = {
        'book': current_book,
    }

    return render(request, 'book-details.html', context)


def profile(request):
    personal_profile = get_profile()
    context = {
        'profile': personal_profile,
    }

    return render(request, 'profile.html', context)


def profile_create(request):
    books = get_books()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home-with-profile.html')

    else:
        form = CreateProfileForm()

        context = {
            'form': form,
            'books': books,
        }

        return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    current_profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=current_profile)

        context = {
            'profile': current_profile,
            'form': form,
        }
        return render(request, 'edit-profile.html', context)


def profile_delete(request):
    current_profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = DeleteProfileForm(instance=current_profile)

        context = {
            'profile': current_profile,
            'form': form,
        }
        return render(request, 'delete-profile.html', context)



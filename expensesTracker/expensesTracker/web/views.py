from django.shortcuts import render, redirect

# Create your views here.
from expensesTracker.web.forms import CreateProfileForm, DeleteProfileForm, CreateExpenseForm, EditExpenseForm, \
    DeleteExpenseForm
from expensesTracker.web.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None  # or "we have profile" to check if page works


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    budget_left = profile.budget - sum(e.price for e in expenses)
    expenses_count = len(expenses)

    context = {
        'profile': profile,
        'expenses_count': expenses_count,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


# main difference from Create is adding the instance
def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = CreateProfileForm(request.POST, request.FILES, instance=profile)  # add instance
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)  # add instance
        if form.is_valid():
            form.save()
            profile.budget = 0
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)

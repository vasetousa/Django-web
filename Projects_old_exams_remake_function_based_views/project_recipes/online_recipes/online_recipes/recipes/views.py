from django.shortcuts import render, redirect

# Create your views here.
from online_recipes.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from online_recipes.recipes.models import Recipe


def get_recipes():
    recipes = Recipe.objects.all()
    if recipes:
        return recipes
    return None


def index(request):
    current_recipe = get_recipes()

    context = {
        'current_recipe': current_recipe,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateRecipeForm()
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)


def edit(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = EditRecipeForm(request.POST, request.FILES, instance=current_recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditRecipeForm(instance=current_recipe)
        context = {
            'form': form,
            'current_recipe': current_recipe,
        }

        return render(request, 'edit.html', context)


def delete(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteRecipeForm(request.POST, request.FILES, instance=current_recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteRecipeForm(instance=current_recipe)
        context = {
            'form': form,
            'current_recipe': current_recipe,
        }

        return render(request, 'delete.html', context)


def details(request, pk):
    current_recipe = Recipe.objects.get(pk=pk)
    ingr = current_recipe.ingredients.split(', ')
    context = {
        'current_recipe': current_recipe,
        'ingr': ingr
    }
    return render(request, 'details.html', context)

from django import forms

from online_recipes.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''  # removes the ":" in the form in this case. "" could be anything

    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time(Minutes)',
        }


class EditRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''  # removes the ":" in the form in this case. "" could be anything

    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time(Minutes)',
        }


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''  # removes the ":" in the form in this case. "" could be anything
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time(Minutes)',
        }

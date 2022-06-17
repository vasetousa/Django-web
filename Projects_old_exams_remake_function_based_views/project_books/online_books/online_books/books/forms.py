from django import forms

from online_books.books.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'URL'}),
        }


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            "description": forms.Textarea(
                attrs={"rows": "100", "cols": "40", "id": "description",
                       'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime...'}),
        }


class EditBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            "description": forms.Textarea(
                attrs={"rows": "100", "cols": "40", "id": "description",
                       'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime...'}),
        }


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        Profile.objects.all().delete()
        Book.objects.all().delete()  # to delete all book object
        return self.instance

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }

from django import forms

from books.online_books.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''  # removes the ":" in the form in this case. "" could be anything

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'URL'}),
        }


class AddBookPage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            "description": forms.Textarea(
                attrs={"name": "description", "rows": "100", "cols": "40", "required": "", "id": "description",
                       "placeholder": "Description"}),
            # 'description': forms.TextInput(attrs={'placeholder': 'Description', }),
            'image': forms.TextInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime...'}),
        }


class EditPageForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label_suffix = ''

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
        # self.fields.widget.attrs['disabled'] = 'disabled'
        # self.fields.required = False
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

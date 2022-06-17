from django import forms

from online_music.music_app.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age',
                }
            )
        }


class CreateAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price',
        }
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'}),
            'description': forms.Textarea(
                attrs={
                    'rows': '100', 'cols': '40', 'placeholder': 'Description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            )

        }


class EditAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price',
        }
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'}),
            'description': forms.Textarea(
                attrs={
                    'rows': '100', 'cols': '40', 'placeholder': 'Description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            )

        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields.widget.attrs['disabled'] = 'disabled'
        # self.fields.required = False
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price',
        }
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'}),
            'description': forms.Textarea(
                attrs={
                    'rows': '100', 'cols': '40', 'placeholder': 'Description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            )

        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()

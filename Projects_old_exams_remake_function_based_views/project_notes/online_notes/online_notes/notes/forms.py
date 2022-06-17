from django import forms

from online_notes.notes.models import Note


class CreateNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'title': 'Title',
            'image_url': 'Link to Image',
            'content': 'Content',
        }


class EditNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'title': 'Title',
            'image_url': 'Link to Image',
            'content': 'Content',
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'title': 'Title',
            'image_url': 'Link to Image',
            'content': 'Content',
        }

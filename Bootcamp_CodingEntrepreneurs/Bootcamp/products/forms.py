from django import forms


from Bootcamp.products.models import Product


class DataForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
        ]

    def clean_title(self):
        data1 = self.cleaned_data.get('title')
        if len(data1) < 4:
            raise forms.ValidationError('Title is too short. Minimum 4 characters')
        return data1

    def clean_content(self):
        data2 = self.cleaned_data.get('content')
        if len(data2) < 4:
            raise forms.ValidationError('Title is too short. Minimum 4 characters')
        return data2


class InventoryWaitlistForm(forms.ModelForm):
    pass


import os

from django import forms

from expensesTracker.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # points which model to use
        fields = ('budget', 'first_name', 'last_name', 'profile_image')  # or use '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image'
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # points which model to use
        fields = ('budget', 'first_name', 'last_name', 'profile_image')  # we can forbid a field for editing


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):  # overrides the save() method from the view and 'deletes' instead
        if commit:
            self.instance.delete()
            image_path = self.instance.profile_image.path  # deletes the profile image too
            Expense.objects.all().delete()  # DELETES ALL EXPENSES
            os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile  # points which model to use
        fields = ()  # we can forbid a field for editing


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense  # points which model to use
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'image': 'Link to Image'
        }


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense  # points which model to use
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'image': 'Link to Image'
        }


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense  # points which model to use
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'image': 'Link to Image'
        }

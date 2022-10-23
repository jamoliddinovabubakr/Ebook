from django import forms

from .models import Book


class AddBookForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['author'].empty_label = 'Category do not choice'

    class Meta:
        model = Book
        fields = ['name', 'author']


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=255)

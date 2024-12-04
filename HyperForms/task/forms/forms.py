from django import forms
from .models import RegisterFormModel

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterFormModel
        fields = ['name', 'age', 'favorite_book']
        labels = {
            'name': 'your name',
            'age': 'your age',
            'favorite_book': 'your favorite book',
        }
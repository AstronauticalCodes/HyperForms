from cProfile import label
from django.db import models
from django import forms


# class RegisterForm(forms.Form):
#     name = forms.CharField(label='your name', max_length=100)
#     age = forms.IntegerField(label='your age')
#     favorite_book = forms.CharField(label='your favorite book', max_length=200)

class RegisterFormModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    favorite_book = models.CharField(max_length=200)
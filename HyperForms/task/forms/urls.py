from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.RegisterFormView.as_view(), name='register'),
]

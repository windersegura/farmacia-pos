from django.contrib import admin
from django.urls import path, re_path, include
from .views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view()),
]
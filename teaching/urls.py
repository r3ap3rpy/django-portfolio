from django.urls import path
from . import views

urlpatterns = [
    path('teaching/', views.teaching, name = "teaching"),
]
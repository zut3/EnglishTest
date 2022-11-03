from django.urls import path
from . import views

urlpatterns = [
    path('new', views.LoadImage.as_view()),
]

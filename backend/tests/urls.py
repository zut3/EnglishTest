from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view()),
    path('new', views.CreateView.as_view())
]

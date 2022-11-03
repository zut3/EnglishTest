from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestsView.as_view()),
    path('new', views.CreateTests.as_view())
]

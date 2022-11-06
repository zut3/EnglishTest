from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'(?P<pk>[\w-]+)?', views.ListView.as_view()),
    path('new', views.CreateView.as_view())
]

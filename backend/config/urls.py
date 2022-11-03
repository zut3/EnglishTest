from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('tests/', include('tests.urls')),
    path('steps/', include('steps.urls')),
    path('answers/', include('answers.urls')),
]

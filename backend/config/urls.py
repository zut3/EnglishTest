from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('storage/', include('storage.urls')),
    path('tests/', include('tests.urls')),
    path('steps/', include('steps.urls')),
    path('answers/', include('answers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

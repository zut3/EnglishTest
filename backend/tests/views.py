from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from serializers import main as serializers
from . import models
from shared.views import BaseRetrieveListView


class CreateView(generics.CreateAPIView):
    serializer_class = serializers.TestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(who_create_id=self.request.user.id)


class ListView(BaseRetrieveListView):
    serializer_class = serializers.TestSerializer

    def get_queryset(self):
        return models.Test.objects.all()


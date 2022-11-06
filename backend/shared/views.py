from rest_framework import generics


class BaseRetrieveListView(generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


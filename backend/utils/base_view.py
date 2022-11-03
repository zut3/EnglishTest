import functools
from rest_framework.response import Response

def base_view(fn):

    @functools.wraps(fn)
    def inner(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as ex:
            print(ex)
            return Response({"error" : str(ex)}, status=400)
    return inner

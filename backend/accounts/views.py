from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import accounts as serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError


@api_view(['POST'])
def user_login(request):
    ser = serializers.UserSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=400)
    
    try:    
        user = ser.save()
    except IntegrityError:
        user = authenticate(request, **ser.validated_data)

    token = Token.objects.get(user=user)
    return Response({"token": token.key})


from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import CredentialSerializer, DeviceLoginSerializer,StatusUpdateSerialize
from django.http import JsonResponse
from rest_framework.decorators import api_view
from mapapp.models import Credential
from .serializers import CredentialSerializer



 # Using the new serializer name

@api_view(['POST'])
def login_gps(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    user = Credential.objects.filter(username=username, password=password).first()
    if user:
        # Successfully found the user. You can return other data if needed.
        return JsonResponse({"success": True, "message": "Logged in successfully"}, status=200)
    else:
        return JsonResponse({"success": False, "message": "Invalid username or password"}, status=401)


@api_view(['PUT'])
def update_credential(request, username):
    try:
        credential = Credential.objects.get(username=username)
    except Credential.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CredentialSerializer(credential, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusUpdateSerializer:
    pass


@api_view(['PUT'])
def status_update_credential(request, username):
    try:
        credential = Credential.objects.get(username=username)
    except Credential.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Use the correct serializer
    serializer = StatusUpdateSerializer(credential, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render

# Create your views here.

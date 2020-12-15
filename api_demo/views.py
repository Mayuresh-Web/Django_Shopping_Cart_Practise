from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Hello'}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'POST'])
def user_detail(request, pk):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=pk)
            return JsonResponse({'name': user.name, 'email': user.email, 'phone_no': user.phone_no, 'age': user.age},
                                status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return JsonResponse({'message': 'Success'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        try:
            user = User.objects.get(pk=pk)
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.update(user, user_data)
            return JsonResponse({'message': 'Success'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def user_count(request):
    count = User.objects.all()
    lenOfUsers = len(count)
    return JsonResponse({'count': lenOfUsers}, status=status.HTTP_200_OK)

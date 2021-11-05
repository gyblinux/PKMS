from django.shortcuts import render
from rest_framework import generics
from users.models import CustomUser
from users.serializers import CustomUserSerializer
# Create your views here.
class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from app import serializers
from app.models import Post
from app.models import Para
from app.serializers import PostSerializer
from app.serializers import ParaSerializer
from rest_framework import generics
# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class ParaList(generics.ListCreateAPIView):
    queryset = Para.objects.all()
    serializer_class = ParaSerializer
class ParaDetail(generics.RetrieveAPIView):
    queryset = Para.objects.all()
    serializer_class = ParaSerializer
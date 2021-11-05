from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Para, Post
from app.serializers import ParaSerializer, PostSerializer

# Create your views here.
# @api_view(['GET'])
@csrf_exempt
def para_list(request):
    if request.method == 'GET':
        paras = Para.objects.all()
        serializer = ParaSerializer(paras, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def post(request):
    if request.method == 'GET':
        post = Post.objects.get(pk=1)
        serializer = PostSerializer(post, many=False)
        return JsonResponse(serializer.data, safe=False)
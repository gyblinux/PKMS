from app.serializers import PostSerializer

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.models import CustomUser
from users.serializers import CustomUserSerializer, RegistrationSerializer
from users.serializers import LoginSerializer
# Create your views here.
class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

class UserLogin(APIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            "success": "True",
            "status_code": status.HTTP_200_OK,
            "message": "User has logged in successfully",
            "id": serializer.validated_data['userid'],
            "token": serializer.validated_data['token']
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

class UserPostsList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        u_pk: int = self.kwargs['pk']
        u = CustomUser.objects.get(pk=u_pk)
        queryset = u.posts.all()
        return queryset

class UserPostsDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self):
        u_pk: int = self.kwargs['pk']
        u = CustomUser.objects.get(pk=u_pk)
        post = u.posts.get(post_id=self.kwargs['post_id'])
        return post
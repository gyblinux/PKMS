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
    """
    Entry point: 
        api/users/
    Render: 
        all the users registered
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    Entry point:
        api/users/<int:user_pk>/
    Permission:
        logged in user with JWT token as the HTTP header
    Render:
        all information from the user model
    """
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    

class UserCreate(generics.CreateAPIView):
    """
    Entry point:
        api/users/register/
    Render:
        new user account in the DB
    """
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

class UserLogin(APIView):
    """
    Entry point:
        api/users/login/
    Render:
        login information with JWT token
    """
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
    """
    Entry point:
        api/users/<int:user_pk>/posts/
    Render:
        all posts of the logged in user
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        u_pk: int = self.kwargs['pk']
        u = CustomUser.objects.get(pk=u_pk)
        queryset = u.posts.all()
        return queryset

class UserPostsDetail(generics.RetrieveAPIView):
    """
    Entry point:
        api/users/<int:user_pk>/posts/<int:post_pk>/
    Render:
        named post detail of current logged in user (with full list of paras)
    """
    serializer_class = PostSerializer

    def get_object(self):
        u_pk: int = self.kwargs['pk']
        u = CustomUser.objects.get(pk=u_pk)
        post = u.posts.get(post_id=self.kwargs['post_id'])
        return post
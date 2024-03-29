from app.models import Post
from app.models import Para
from app.serializers import PostSerializer
from app.serializers import ParaSerializer

from rest_framework import generics     # integrated mixin views
from rest_framework import permissions  # browsable api auth
from app.permissions import IsOwnerOrReadOnly # object-level restrictions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })
class PostListCreate(generics.ListCreateAPIView):
    """integrated generics mixin view for: Post model-list/creation"""
    queryset = Post.objects.all()       
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # rest_framework api-auth setting

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) # self.request.user = AUTH_USER_MODEL in project-settings
class PostDetail(generics.RetrieveAPIView):
    """integrated generics mixin view for: Post single detail"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # rest_framework api-auth setting
    permission_classes += [IsOwnerOrReadOnly] # permissions
class ParaListCreate(generics.ListCreateAPIView):
    queryset = Para.objects.all()
    serializer_class = ParaSerializer
class ParaDetail(generics.RetrieveAPIView):
    queryset = Para.objects.all()
    serializer_class = ParaSerializer
from rest_framework import serializers
from users.models import CustomUser
from app.models import Para, Post

class CustomUserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'posts'] # adding related_name='posts' explicitly
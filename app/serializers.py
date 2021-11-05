from rest_framework import serializers
from app.models import Post, Para

class ParaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Para
        # fields = '__all__'
        fields = ['para_id', 'content', 'previous', 'of_post'] # explicitly add 'of_post'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
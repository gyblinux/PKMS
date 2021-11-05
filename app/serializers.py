from rest_framework import serializers
from app.models import Post, Para

class ParaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Para
        # fields = '__all__'
        fields = ['para_id', 'content', 'previous', 'of_post', 'next'] # explicitly add 'of_post'
        read_only_fields = ['of_post', 'next'] # do not validate or require input of the 'of_post' field

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
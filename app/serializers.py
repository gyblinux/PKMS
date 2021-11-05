from rest_framework import serializers
from app.models import Post, Para

class ParaSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     return Para.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance
    class Meta:
        model = Para
        # fields = '__all__'
        fields = ['para_id', 'content', 'previous', 'of_post'] # explicitly add 'of_post'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
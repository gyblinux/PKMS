from rest_framework import serializers
from app.models import Post, Para

class ParaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Para
        # fields = '__all__'
        fields = ['para_id', 'content', 'previous', 'of_post', 'next'] # explicitly add 'of_post'
        read_only_fields = ['of_post', 'next'] # do not validate or require input of the 'of_post' field

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    paras = serializers.SerializerMethodField('get_serialized_paras') # must be serialized obj, otherwise cannot be rendered

    def get_serialized_paras(self, obj):
        raw_paras = obj.render_paras # property
        return ParaSerializer(raw_paras, many=True).data
    class Meta:
        model = Post
        # fields = '__all__'.
        fields = ['post_id', 'owner', 'is_shared', 'last_modified', 'post_title', 'index_para', 'paras']
        read_only_fields = ['owner']
from rest_framework import serializers
from .models import Blog, Comment, Like, Tag
from apps.user.serializers import UserSerializer

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    tags = TagsSerializer(many=True, required=False)

    class Meta:
        model = Blog
        fields = ['id', 'user', 'video', 'title', 'description', 'create_at', 'tags']

class CommentSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(many=True, required=False)
    user = UserSerializer(many=True, required=False)

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(many=True, required=False)
    user = UserSerializer(many=True, required=False)

    class Meta:
        model = Like
        fields = ['blog', 'user']
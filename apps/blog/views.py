from django.shortcuts import render
from rest_framework import generics, viewsets
from django.shortcuts import render

from .models import Blog, Comment, Like, Tag
from .serializers import BlogSerializer, CommentSerializer, LikeSerializer, TagsSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-create_at')
    serializer_class = BlogSerializer


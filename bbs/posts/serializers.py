from rest_framework import serializers
from users.serializers import ProfileSerializer
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ("pk","profile", "post", "text")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("pk","profile","title", "body", "image", "published_date", "likes")


class PostCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=True)
    
    class Meta:
        model = Post
        fields = ("profile", "category", "body", "image")
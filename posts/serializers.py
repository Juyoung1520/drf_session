# posts > serializers.py
# 주의! DRF는 TextField를 지원하지 않음. -> CharField로 내부적으로 긴 문자열을 받을 수 있음.
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment

# 기본 serializer
class PostBaseSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    view_count = serializers.IntegerField(required=False)
    writer = serializers.IntegerField()
    bad_post = serializers.BooleanField(required=False)


    def create(self, validated_data):
        writer_id = validated_data['writer']
        writer = get_user_model().objects.get(pk=writer_id)

        # 'view_count' 필드가 요청에 없는 경우를 대비하여 기본값 설정
        view_count = validated_data.get('view_count',0)

        post = Post.objects.create(
            content = validated_data['content'],
            view_count = view_count,
            writer = writer,
        )
        return post
    
class CommentCreateSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=255)
    post = serializers.IntegerField()
    writer = serializers.IntegerField()


    def create(self, validated_data):
        writer_id = validated_data.pop('writer')
        writer = get_user_model().objects.get(pk=writer_id)
        post_id = validated_data.pop('post')
        post = Post.objects.get(pk=post_id)

        return Comment.objects.create(post=post, writer = writer, **validated_data) #주어진 'post' 객체와 검증된 데이터를 사용해 새로운 댓글을 생성하고 반환한다.

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


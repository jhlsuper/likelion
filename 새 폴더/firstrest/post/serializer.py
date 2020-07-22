from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #filels = '__all__' 밑에거랑 같게 나옴
        fields= ['id','title','body']
        read_only_fields =('title',)